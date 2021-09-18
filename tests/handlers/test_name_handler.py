import ast
import unittest
from obscurepy.handlers.name_handler import NameHandler
from obscurepy.handlers.name_handler import obscure_class_bases, \
    handle_class_scope, handle_global_scope, handle_function_scope, handle_calls, handle_returns
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.handlers.functiondef_handler import FunctionDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.tree import add_parents


"""
Make sure self.source contains these examples

NameHandler handles:
    * Base classes of a ClassDef
    * Variable side of assignments: global scope, class scope, function scope
    * Function returns
    * ast.Name nodes inside of ast.Call nodes, ie. (a = some_function(), a = SomeClass())
"""


class TestNameHandler(unittest.TestCase):

    def setUp(self):
        self.fixture = NameHandler()
        self.classdef_handler = ClassDefHandler()
        self.source = 'class Base1:\n\t' \
                      'pass\n\n' \
                      'class Base2:\n\t' \
                      'pass\n\n' \
                      'class SomeClass(Base1, Base2):\n\t' \
                      'pass\n' \
                      'def first_function():\n\t' \
                      'pass\n' \
                      'def some_function():\n\t' \
                      'a = "a literal"\n\t' \
                      'b = first_function()\n\t' \
                      'return b'

        self.tree = ast.parse(self.source)
        add_parents(self.tree)

    def tearDown(self):
        tracker = DefinitionTracker.get_instance()
        tracker.clear_definitions()

    def test_visitName(self):
        self.tree = self.classdef_handler.handle(self.tree)
        self.tree = self.fixture.handle(self.tree)
        self.assertEqual(self.tree.body[2].bases[0].id, '_0x1ac')
        self.assertEqual(self.tree.body[2].bases[1].id, '_0x1ad')

    def test_obscure_class_bases(self):
        tree = ast.parse('class SomeClass(Base1, Base2):\n\tpass')
        add_parents(tree)
        bases = []
        tracker = DefinitionTracker.get_instance()
        tracker.definitions['classes']['Base1'] = {'prev_name': 'Base1',
                                                   'new_name': 'ObscuredBase1'}
        tracker.definitions['classes']['Base2'] = {'prev_name': 'Base2',
                                                   'new_name': 'ObscuredBase2'}
        for base in tree.body[0].bases:
            bases.append(obscure_class_bases(base, tracker))
        self.assertEqual(bases[0].id, 'ObscuredBase1')
        self.assertEqual(bases[1].id, 'ObscuredBase2')

    def test_handle_function_scope(self):
        tree = ast.parse('def some_function():\n\ta = 42')
        add_parents(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_function_scope(
            tree.body[0].body[0].targets[0], tracker)
        self.assertEqual(handled_node.id, '_0x61')

    def test_handle_function_scope_outside(self):
        tree = ast.parse('def some_function():\n\tpass\na = 42')
        add_parents(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_function_scope(tree.body[1].targets[0], tracker)
        self.assertEqual(handled_node, tree.body[1].targets[0])

    def test_handle_global_scope(self):
        tree = ast.parse('a = "some string"')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_global_scope(tree.body[0].targets[0], tracker)
        self.assertEqual(handled_node.id, '_0x61')
        self.assertEqual(len(tracker.definitions['variables']), 1)

    def test_handle_global_scope_outside(self):
        tree = ast.parse('def some_function():\n\tsome_variable = 42')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_global_scope(
            tree.body[0].body[0].targets[0], tracker)
        self.assertEqual(handled_node, tree.body[0].body[0].targets[0])
        self.assertEqual(len(tracker.definitions['variables']), 0)

    def test_handle_class_scope(self):
        tree = ast.parse('class SomeClass:\n\tclass_variable = 42')
        add_parents(tree)
        tree = ClassDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_class_scope(
            tree.body[0].body[0].targets[0], tracker)
        self.assertEqual(handled_node.id, '_0x5bb')
        self.assertEqual(
            len(tracker.definitions['classes']['SomeClass']['variables']), 1)

    def test_handle_class_scope_outside(self):
        tree = ast.parse('class SomeClass:\n\tpass\nvariable = 42')
        add_parents(tree)
        tree = ClassDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_class_scope(tree.body[1].targets[0], tracker)
        self.assertEqual(handled_node, tree.body[1].targets[0])
        self.assertEqual(
            len(tracker.definitions['classes']['SomeClass']['variables']), 0)

    def test_handle_calls_class(self):
        tree = ast.parse(
            'class SomeClass:\n\tpass\nsome_variable = SomeClass()')
        add_parents(tree)
        tree = ClassDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_calls(tree.body[1].value.func, tracker)
        self.assertEqual(handled_node.id, '_0x38a')

    def test_handle_calls_function(self):
        tree = ast.parse(
            'def some_function():\n\tpass\nsome_variable = some_function()')
        add_parents(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_calls(tree.body[1].value.func, tracker)
        self.assertEqual(handled_node.id, '_0x579')

    def test_handle_calls_func_in_func(self):
        tree = ast.parse(
            'def some_function():\n\tdef inside_function():\n\t\tpass\n\tsome_variable = inside_function()')
        add_parents(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_calls(tree.body[0].body[1].value.func, tracker)
        self.assertEqual(handled_node.id, '_0x641')

    def test_handle_calls_outside(self):
        tree = ast.parse('a = 42')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_calls(tree.body[0].targets[0], tracker)
        self.assertEqual(handled_node, tree.body[0].targets[0])

    def test_handle_returns_class(self):
        tree = ast.parse(
            'class SomeClass:\n\tpass\ndef some_function():\n\treturn SomeClass()')
        add_parents(tree)
        tree = ClassDefHandler().handle(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_returns(tree.body[1].body[0].value.func, tracker)
        self.assertEqual(handled_node.id, '_0x38a')

    def test_handle_returns_function(self):
        tree = ast.parse(
            'def some_function():\n\tpass\ndef another_function():\n\treturn some_function()')
        add_parents(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_returns(tree.body[1].body[0].value.func, tracker)
        self.assertEqual(handled_node.id, '_0x579')

    def test_handle_returns_func_in_func(self):
        tree = ast.parse(
            'def some_function():\n\tdef inside_function():\n\t\tpass\n\treturn inside_function()')
        add_parents(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_returns(tree.body[0].body[1].value.func, tracker)
        self.assertEqual(handled_node.id, '_0x641')

    def test_handle_returns_variable(self):
        tree = ast.parse(
            'def some_function():\n\tsome_variable = 42\n\treturn some_variable')
        add_parents(tree)
        tree = FunctionDefHandler().handle(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_returns(tree.body[0].body[1].value, tracker)
        self.assertEqual(handled_node.id, '_0x559')

    def test_handle_returns_none(self):
        tree = ast.parse('def some_function():\n\tsome_variable = 42')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_returns(tree.body[0].body[0].targets[0], tracker)
        self.assertEqual(handled_node, tree.body[0].body[0].targets[0])

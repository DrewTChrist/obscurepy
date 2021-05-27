import ast
import unittest
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.handlers.functiondef_handler import FunctionDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.handlers.functiondef_handler import get_args, get_variables, get_return
from obscurepy.handlers.functiondef_handler import handle_function_scope, handle_class_scope, handle_global_scope
from obscurepy.utils.tree import add_parents


class FunctionDefHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = FunctionDefHandler()
        self.classdef_handler = ClassDefHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.source = 'def FirstFunction(param_1, param_2):\n\t' \
                      'first_variable = 42\n\t' \
                      'second_variable = param_1 + param_2\n\t' \
                      'return second_variable\n' \
                      'class SomeClass():\n\t' \
                      'def some_method():\n\t\t' \
                      'pass'
        self.tree = ast.parse(self.source)
        add_parents(self.tree)
        self.tree = self.classdef_handler.handle(self.tree)

    def tearDown(self):
        self.tracker.clear_definitions()

    def test_visitFunctionDef(self):
        self.tree = self.fixture.handle(self.tree)
        self.assertEqual(len(self.tracker.definitions['functions']), 1)
        function = self.tracker.definitions['functions']['FirstFunction']
        self.assertEqual(function['new_name'], '_0x54e')
        self.assertEqual(function['prev_name'], 'FirstFunction')
        self.assertEqual(function['variables']['first_variable'], '_0x5cd')
        self.assertEqual(function['args']['param_1'], '_0x2a1')
        self.assertEqual(function['return']['second_variable'], '_0x621')

    def test_get_args(self):
        args = get_args(self.tree.body[0])
        self.assertEqual(args['param_1'], '_0x2a1')
        self.assertEqual(args['param_2'], '_0x2a2')

    def test_get_args_none(self):
        tree = ast.parse('def FirstFunction():\n\tpass')
        args = get_args(tree.body[0])
        self.assertTrue(len(args) == 0)

    def test_get_variables(self):
        variables = get_variables(self.tree.body[0])
        self.assertEqual(variables['first_variable'], '_0x5cd')
        self.assertEqual(variables['second_variable'], '_0x621')

    def test_get_variables_none(self):
        tree = ast.parse('def FirstFunction():\n\tpass')
        variables = get_variables(tree.body[0])
        self.assertTrue(len(variables) == 0)

    def test_get_return(self):
        return_ = get_return(self.tree.body[0])
        self.assertEqual(return_['second_variable'], '_0x621')

    def test_get_return_none(self):
        tree = ast.parse('def a_function():\n\tpass')
        return_ = get_return(tree.body[0])
        self.assertEqual(len(return_), 0)

    def test_handle_global_scope(self):
        tree = ast.parse('def global_function():\n\tpass')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_global_scope(tree.body[0], tracker)
        self.assertTrue('global_function' in tracker.definitions['functions'])

    def test_handle_global_scope_outside(self):
        tree = ast.parse(
            'def global_function():\n\tdef function_function():\n\t\tpass')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_global_scope(tree.body[0].body[0], tracker)
        self.assertEqual(len(tracker.definitions['functions']), 0)

    def test_handle_class_scope(self):
        tree = ast.parse('class SomeClass:\n\tdef some_method():\n\t\tpass')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_class_scope(tree.body[0].body[0], tracker)
        self.assertTrue(
            len(tracker.definitions['classes']['SomeClass']['methods']), 1)

    def test_handle_class_scope_outside(self):
        tree = ast.parse(
            'def some_function():\n\tpass\nclass SomeClass:\n\tpass')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_class_scope(tree.body[0], tracker)
        self.assertTrue(
            'some_function' not in tracker.definitions['classes']['SomeClass']['methods'])

    def test_handle_function_scope(self):
        tree = ast.parse(
            'def global_function():\n\tdef function_function():\n\t\tpass')
        add_parents(tree)
        tracker = DefinitionTracker.get_instance()
        handled_node = handle_function_scope(tree.body[0].body[0], tracker)
        pass

    def test_handle_function_scope_outside(self):
        pass

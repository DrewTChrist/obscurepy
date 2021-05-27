import ast
import unittest
from obscurepy.handlers.name_handler import NameHandler
from obscurepy.handlers.name_handler import obscure_class_bases, \
    handle_class_scope, handle_global_scope, handle_function_scope
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.tree import add_parents


class TestNameHandler(unittest.TestCase):

    def setUp(self):
        self.fixture = NameHandler()
        self.classdef_handler = ClassDefHandler()
        self.source = 'class Base1:\n\tpass\n\nclass Base2:\n\tpass\n\nclass SomeClass(Base1, Base2):\n\tpass'
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
        pass

    def test_handle_function_scope_outside(self):
        pass

    def test_handle_global_scope(self):
        pass

    def test_handle_global_scope_outside(self):
        pass

    def test_handle_class_scope(self):
        pass

    def test_handle_class_scope_outside(self):
        pass

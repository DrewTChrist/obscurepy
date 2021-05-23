import ast
import unittest
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.handlers.classdef_handler import create_class_dictionary
from obscurepy.handlers.classdef_handler import get_base_classes
from obscurepy.handlers.classdef_handler import get_methods
from obscurepy.handlers.classdef_handler import get_properties
from obscurepy.handlers.classdef_handler import get_variables


class ClassDefHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ClassDefHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.tracker.clear_definitions()
        self.source = 'class TestClass(BaseClass):\n\t' \
                      'eighty_four = 84\n\t' \
                      'def __init__(self):\n\t\t' \
                      'self.forty_two = 42'
        self.tree = ast.parse(self.source)

    def test_visitClassDef(self):
        self.tree = self.fixture.handle(self.tree)
        self.assertEqual(len(self.tracker.definitions['classes']), 1)

    def test_create_class_dictionary(self):
        class_dict = create_class_dictionary(self.tree.body[0])
        self.tracker.add_class(class_dict)
        class_ = self.tracker.definitions['classes']['TestClass']
        self.assertEqual(class_['new_name'], '_0x397')
        self.assertEqual(class_['prev_name'], 'TestClass')
        self.assertEqual(class_['variables'][0], 'eighty_four')
        self.assertEqual(class_['properties'][0], 'forty_two')
        self.assertEqual(class_['methods'][0], '__init__')
        self.assertEqual(class_['bases'][0], 'BaseClass')

    def test_get_variables(self):
        variables = get_variables(self.tree.body[0])
        self.assertEqual(variables[0], 'eighty_four')

    def test_get_variables_none(self):
        tree = ast.parse('class TestClass:\n\tpass')
        variables = get_variables(tree)
        self.assertTrue(len(variables) == 0)

    def test_get_properties(self):
        properties = get_properties(self.tree.body[0])
        self.assertEqual(properties[0], 'forty_two')

    def test_get_properties_none(self):
        tree = ast.parse('class TestClass:\n\tpass')
        properties = get_properties(tree)
        self.assertTrue(len(properties) == 0)

    def test_get_methods(self):
        methods = get_methods(self.tree.body[0])
        self.assertEqual(methods[0], '__init__')

    def test_get_methods_none(self):
        tree = ast.parse('class TestClass:\n\tpass')
        methods = get_methods(tree)
        self.assertTrue(len(methods) == 0)

    def test_get_base_classes(self):
        bases = get_base_classes(self.tree.body[0])
        self.assertEqual(bases[0], 'BaseClass')

    def test_get_base_classes_none(self):
        tree = ast.parse('class TestClass:\n\tpass')
        bases = get_base_classes(tree)
        self.assertTrue(len(bases) == 0)

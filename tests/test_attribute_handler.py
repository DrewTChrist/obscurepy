import ast
import unittest
from obscurepy.handlers.attribute_handler import AttributeHandler, handle_class_properties
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.tree import add_parents


class AttributeHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = AttributeHandler()
        self.classdef_handler = ClassDefHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.source = 'class SomeClass:\n\tdef __init__():\n\t\tself.property = 42\n\t\tself.property2 = 84'
        self.tree = ast.parse(self.source)
        add_parents(self.tree)
        self.tree = self.classdef_handler.handle(self.tree)

    def tearDown(self):
        self.tracker.clear_definitions()

    def test_visit_Attribute(self):
        self.tree = self.fixture.handle(self.tree)
        self.assertEqual(
            self.tree.body[0].body[0].body[0].targets[0].attr, '_0x385')
        self.assertEqual(
            self.tree.body[0].body[0].body[1].targets[0].attr, '_0x3b7')

    def test_handle_class_properties(self):
        handled_node = handle_class_properties(
            self.tree.body[0].body[0].body[0].targets[0], self.tracker)
        self.assertEqual(handled_node.attr, '_0x385')
        handled_node = handle_class_properties(
            self.tree.body[0].body[0].body[1].targets[0], self.tracker)
        self.assertEqual(handled_node.attr, '_0x3b7')

    def test_handle_class_properties_outside_init(self):
        tree = ast.parse(
            'class SomeClass:\n\tdef some_method():\n\t\tself.new_property = 42')
        add_parents(tree)
        tree = self.classdef_handler.handle(tree)
        handled_node = handle_class_properties(
            tree.body[0].body[0].body[0].targets[0], self.tracker)
        self.assertEqual(handled_node.attr, '_0x52e')

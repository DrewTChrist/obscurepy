import ast
import unittest
from obscurepy.utils.tree import *


class GeneralTest(unittest.TestCase):

    def setUp(self):
        self.class_source = 'class TestClass:\n\n\tdef class_function():\n\t\tpass'
        self.func_source = 'def test_function():\n\ta = 1'
        self.class_tree = ast.parse(self.class_source)
        add_parents(self.class_tree)
        self.func_tree = ast.parse(self.func_source)
        add_parents(self.func_tree)

    def tearDown(self):
        pass

    def test_add_parents(self):
        add_parents(self.class_tree)
        self.assertTrue(self.class_tree.body[0].parent is not None)

    def test_get_node_type(self):
        self.assertEqual(get_node_type(
            self.class_tree.body[0].body[0]), ast.FunctionDef)

    def test_is_parent_of_type(self):
        self.assertTrue(has_parent_of_type(
            self.class_tree.body[0].body[0], ast.ClassDef))

    def test_is_in_function_scope(self):
        self.assertTrue(is_in_function_scope(self.func_tree.body[0].body[0]))

    def test_get_parent_function_name(self):
        self.assertEqual(get_parent_function_name(
            self.func_tree.body[0].body[0]), "test_function")

    def test_get_parent_function_name_outside(self):
        # testing for a node not within the scope of a function
        tree = ast.parse('a = 1')
        add_parents(tree)
        with self.assertRaises(Exception):
            get_parent_function_name(tree.body[0])

    def test_is_in_class_scope(self):
        self.assertTrue(is_in_class_scope(self.class_tree.body[0].body[0]))

    def test_get_parent_class_name(self):
        self.assertTrue(get_parent_class_name(
            self.class_tree.body[0].body[0]), "TestClass")

    def test_get_parent_class_name_outside(self):
        # testing that node is not within a class scope
        tree = ast.parse('a = 1')
        add_parents(tree)
        with self.assertRaises(Exception):
            get_parent_class_name(tree.body[0])

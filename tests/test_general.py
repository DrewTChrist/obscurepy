import ast
import unittest
from obscurepy.treeutils.function_scope_utils import *


class GeneralTest(unittest.TestCase):

    def setUp(self):
        self.source = 'class TestClass:\n\n\tdef class_function():\n\t\tpass'
        self.tree = ast.parse(self.source)

    def tearDown(self):
        pass

    def test_add_parents(self):
        add_parents(self.tree)
        self.assertTrue(self.tree.body[0].parent is not None)

    def test_get_node_type(self):
        self.assertEqual(get_node_type(
            self.tree.body[0].body[0]), ast.FunctionDef)

    def test_is_parent_of_type(self):
        add_parents(self.tree)
        self.assertTrue(has_parent_of_type(
            self.tree.body[0].body[0], ast.ClassDef))

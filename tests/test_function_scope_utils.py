import ast
import unittest
from obscurepy.treeutils.function_scope_utils import *


class FunctionScopeUtilsTest(unittest.TestCase):

    def setUp(self):
        self.source = 'def test_function():\n\ta = 1'
        self.tree = ast.parse(self.source)

    def tearDown(self):
        pass

    def test_is_in_function_scope(self):
        add_parents(self.tree)
        self.assertTrue(is_in_function_scope(self.tree.body[0].body[0]))

    def test_get_parent_function_name(self):
        add_parents(self.tree)
        self.assertEqual(get_parent_function_name(
            self.tree.body[0].body[0]), "test_function")

    def test_get_parent_function_name_outside(self):
        # testing for a node not within the scope of a function
        tree = ast.parse('a = 1')
        add_parents(tree)
        with self.assertRaises(Exception):
            get_parent_function_name(tree.body[0])

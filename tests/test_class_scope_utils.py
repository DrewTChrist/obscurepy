import ast
import unittest
from obscurepy.treeutils.class_scope_utils import *
from obscurepy.treeutils.general import add_parents


class ClassScopeUtilsTest(unittest.TestCase):

    def setUp(self):
        self.source = 'class TestClass:\n\n\tdef class_function():\n\t\tpass'
        self.tree = ast.parse(self.source)

    def tearDown(self):
        pass

    def test_is_in_class_scope(self):
        add_parents(self.tree)
        self.assertTrue(is_in_class_scope(self.tree.body[0].body[0]))

    def test_get_parent_class_name(self):
        add_parents(self.tree)
        self.assertTrue(get_parent_class_name(
            self.tree.body[0].body[0]), "TestClass")

    def test_get_parent_class_name_outside(self):
        # testing that node is not within a class scope
        tree = ast.parse('a = 1')
        add_parents(tree)
        with self.assertRaises(Exception):
            get_parent_class_name(tree.body[0])

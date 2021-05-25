import ast
import unittest
from obscurepy.handlers.constant_handler import *


class ConstantHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ConstantHandler()
        self.source = 'a = "a string literal"\n' \
                      'b = 42\n' \
                      'c = 100.0'
        self.tree = ast.parse(self.source)
        self.tree = self.fixture.handle(self.tree)

    def test_visit_constant(self):
        self.assertEqual(ast.unparse(self.tree.body[0]),
                         "a = ''.join([chr(x) for x in [97, 32, 115, 116, 114, 105, 110, "
                         "103, 32, 108, 105, 116, 101, 114, 97, 108]])")
        self.assertEqual(ast.unparse(self.tree.body[1]), "b = int('0x2a', 16)")
        self.assertEqual(ast.unparse(
            self.tree.body[2]), "c = float.fromhex('0x1.9000000000000p+6')")

    def test_visit_constant_none(self):
        tree = ast.parse('some_function()')
        tree = self.fixture.handle(tree)
        source = ast.unparse(tree)
        self.assertEqual(source, 'some_function()')

    def test_handle_str(self):
        tree = ast.parse('a = "literal"')
        tree = handle_str(tree.body[0].value)
        source = ast.unparse(tree)
        self.assertEqual(
            source, "''.join([chr(x) for x in [108, 105, 116, 101, 114, 97, 108]])")

    def test_handle_int(self):
        tree = ast.parse('a = 1000')
        tree = handle_int(tree.body[0].value)
        source = ast.unparse(tree)
        self.assertEqual(source, "int('0x3e8', 16)")

    def test_handle_float(self):
        tree = ast.parse(ast.parse('a = 10.5'))
        tree = handle_float(tree.body[0].value)
        source = ast.unparse(tree)
        self.assertEqual(source, "float.fromhex('0x1.5000000000000p+3')")

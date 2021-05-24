import ast
import unittest
from obscurepy.handlers.constant_handler import ConstantHandler


class ConstantHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ConstantHandler()
        self.source = 'a = "a string literal"\nb = 42\nc = 84'
        self.tree = ast.parse(self.source)
        self.tree = self.fixture.handle(self.tree)

    def test_str(self):
        pass

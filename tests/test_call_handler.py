import ast
import unittest
from obscurepy.handlers.call_handler import CallHandler
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker


class CallHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = CallHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.classDefHandler = ClassDefHandler()
        self.source = 'class TestClass:\n\tpass\n\na = TestClass()'
        self.tree = self.classDefHandler.handle(ast.parse(self.source))

    def test_visitCall(self):
        pass

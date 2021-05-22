import ast
import unittest
from obscurepy.handlers.function_handler import FunctionHandler
from obscurepy.utils.definition_tracker import DefinitionTracker


class FunctionDefHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = FunctionHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.source = 'def FirstFunction():\n\tpass\n\ndef SecondFunction():\n\tpass'

    def test_visitFunctionDef(self):
        tree = ast.parse(self.source)
        tree = self.fixture.handle(tree)
        self.assertEqual(len(self.tracker.definitions['functions']), 2)

import ast
import unittest
from obscurepy.handlers.call_handler import CallHandler
from obscurepy.utils.definition_tracker import DefinitionTracker


class CallHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = CallHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.tracker.add_class('FirstClass')
        self.source = 'class FirstClass:\n\tpass\n\na = FirstClass()'

    def test_visitCall(self):
        tree = ast.parse(self.source)
        tree = self.fixture.handle(tree)

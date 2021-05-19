import ast
import unittest
from obscurepy.handlers.class_handler import ClassHandler
from obscurepy.utils.definition_tracker import DefinitionTracker


class ClassDefHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ClassHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.source = 'class FirstClass:\n\tpass\n\nclass SecondClass:\n\tpass'

    def test_visitClassDef(self):
        tree = ast.parse(self.source)
        tree = self.fixture.handle(tree)
        print(ast.unparse(tree))
        self.assertEqual(len(self.tracker.definitions['classes']), 2)

import ast
import unittest
from obscurepy.handlers.classdef_handler import ClassDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker


class ClassDefHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ClassDefHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.tracker.clear_definitions()
        self.source = 'class FirstClass:\n\tpass\n\nclass SecondClass:\n\tpass'

    def test_visitClassDef(self):
        tree = ast.parse(self.source)
        tree = self.fixture.handle(tree)
        self.assertEqual(len(self.tracker.definitions['classes']), 2)

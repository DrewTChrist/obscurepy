import ast
import unittest
from obscurepy.handlers.assign_handler import AssignHandler
from obscurepy.utils.definition_tracker import DefinitionTracker


class AssignHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = AssignHandler()
        self.tracker = DefinitionTracker.get_instance()

    def tearDown(self):
        pass

    def test_visitAssign(self):
        pass

import ast
import unittest
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.loader import *
from obscurepy.utils.tree import add_parents


class CompleteChainTest(unittest.TestCase):

    def setUp(self):
        self.fixture = load_handlers(False, False)
        self.tracker = DefinitionTracker.get_instance()
        self.source = 'class FirstClass:\n\tpass\n\n' \
                      'class SecondClass:\n\tpass\n\n' \
                      'def FirstFunction():\n\tc = "a literal"\n\n' \
                      'def SecondFunction():\n\tpass\n\n' \
                      'a = FirstClass()\n\n' \
                      'b = SecondClass()\n\n' \
                      'FirstFunction()\n\n' \
                      'SecondFunction()\n\n' \
                      'a = SecondClass()\n\n' \
                      'c = 42'
        self.tree = ast.parse(self.source)
        add_parents(self.tree)

    def test_complete_chain(self):
        self.tree = self.fixture.handle(self.tree)

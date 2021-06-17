import ast
import unittest
from obscurepy.handlers.arg_handler import ArgHandler, handle_args
from obscurepy.handlers.functiondef_handler import FunctionDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.tree import add_parents


class ArgHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ArgHandler()
        self.functiondef_handler = FunctionDefHandler()
        DefinitionTracker.get_instance().clear_definitions()

    def test_handle_args(self):
        tree = ast.parse(
            'def some_function(param_1, param_2, param_3):\n\tpass')
        add_parents(tree)
        self.functiondef_handler.handle(tree)
        handled_node = handle_args(
            tree.body[0].args.args[0], DefinitionTracker.get_instance())
        self.assertEqual(handled_node.arg, '_0x2a1')

    def test_visit_arg(self):
        tree = ast.parse(
            'def some_function(param_1, param_2, param_3):\n\tpass')
        add_parents(tree)
        tree = self.functiondef_handler.handle(tree)
        tree = self.fixture.handle(tree)
        self.assertEqual(tree.body[0].args.args[0].arg, '_0x2a1')
        self.assertEqual(tree.body[0].args.args[1].arg, '_0x2a2')
        self.assertEqual(tree.body[0].args.args[2].arg, '_0x2a3')

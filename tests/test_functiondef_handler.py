import ast
import unittest
from obscurepy.handlers.functiondef_handler import FunctionDefHandler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.handlers.functiondef_handler import get_args
from obscurepy.handlers.functiondef_handler import get_variables
from obscurepy.handlers.functiondef_handler import get_return
from obscurepy.utils.tree import add_parents


class FunctionDefHandlerTest(unittest.TestCase):

    def setUp(self):
        self.fixture = FunctionDefHandler()
        self.tracker = DefinitionTracker.get_instance()
        self.source = 'def FirstFunction(param_1, param_2):\n\t' \
                      'first_variable = 42\n\t' \
                      'second_variable = param_1 + param_2\n\t' \
                      'return second_variable'
        self.tree = ast.parse(self.source)
        add_parents(self.tree)

    def test_visitFunctionDef(self):
        self.tree = self.fixture.handle(self.tree)
        self.assertEqual(len(self.tracker.definitions['functions']), 1)
        function = self.tracker.definitions['functions']['FirstFunction']
        self.assertEqual(function['new_name'], '_0x54e')
        self.assertEqual(function['prev_name'], 'FirstFunction')
        self.assertEqual(function['variables']['first_variable'], '_0x5cd')
        self.assertEqual(function['args']['param_1'], '_0x2a1')
        self.assertEqual(function['return']['second_variable'], '_0x621')

    def test_get_args(self):
        args = get_args(self.tree.body[0])
        self.assertEqual(args['param_1'], '_0x2a1')
        self.assertEqual(args['param_2'], '_0x2a2')

    def test_get_args_none(self):
        tree = ast.parse('def FirstFunction():\n\tpass')
        args = get_args(tree.body[0])
        self.assertTrue(len(args) == 0)

    def test_get_variables(self):
        variables = get_variables(self.tree.body[0])
        self.assertEqual(variables['first_variable'], '_0x5cd')
        self.assertEqual(variables['second_variable'], '_0x621')

    def test_get_variables_none(self):
        tree = ast.parse('def FirstFunction():\n\tpass')
        variables = get_variables(tree.body[0])
        self.assertTrue(len(variables) == 0)

    def test_get_return(self):
        return_ = get_return(self.tree.body[0])
        self.assertEqual(return_['second_variable'], '_0x621')

    def test_get_return_none(self):
        tree = ast.parse('def FirstFunction():\n\tpass')
        return_ = get_return(tree.body[0])
        self.assertEqual(len(return_), 0)

    def _handle_global_scope(self):
        pass

    def _handle_global_scope_outside(self):
        pass

    def _handle_class_scope(self):
        pass

    def _handle_class_scope_outside(self):
        pass

    def _handle_function_scope(self):
        pass

    def _handle_function_scope_outside(self):
        pass

import unittest
from obscurepy.models.obs_function import ObsFunction
from obscurepy.models.obs_variable import ObsVariable


class ObsClassTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ObsFunction('new name', 'old name', 'return value')

    def test_add_argument(self):
        self.fixture.add_argument(ObsVariable('new var1', 'old var1'))
        self.fixture.add_argument(ObsVariable('new var2', 'old var2'))
        self.assertTrue(len(self.fixture.arguments), 2)

    def test_add_argument_non(self):
        with self.assertRaises(TypeError):
            self.fixture.add_argument('a')

    def test_add_variable(self):
        self.fixture.add_variable(ObsVariable('new var1', 'old var1'))
        self.fixture.add_variable(ObsVariable('new var2', 'old var2'))
        self.assertTrue(len(self.fixture.variables), 2)

    def test_add_variable_non(self):
        with self.assertRaises(TypeError):
            self.fixture.add_variable('a')

    def test_add_function(self):
        self.fixture.add_function(ObsFunction(
            'new func1', 'old func1', 'return val1'))
        self.fixture.add_function(ObsFunction(
            'new func2', 'old func2', 'return val2'))
        self.assertTrue(len(self.fixture.functions), 2)

    def test_add_function_non(self):
        with self.assertRaises(TypeError):
            self.fixture.add_function('a')

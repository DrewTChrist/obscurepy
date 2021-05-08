import unittest
from obscurepy.utils.definition_tracker import DefinitionTracker


class TestDefinitionTracker(unittest.TestCase):

    def setUp(self):
        self.fixture = DefinitionTracker.get_instance()
        self.test_class = {'name': 'test_class',
                           'functions': []}
        self.test_function = {'name': 'test_function',
                              'parameters': []}
        self.test_variable = {'name': 'test_variable'}

    def test_add_class(self):
        self.fixture.add_class(self.test_class)
        self.assertEqual(len(self.fixture.definitions['classes']), 1)

    def test_get_class(self):
        self.fixture.add_class(self.test_class)
        class_ = self.fixture.get_class('test_class')
        self.assertEqual(class_, self.test_class)

    def test_add_function(self):
        self.fixture.add_function(self.test_function)
        self.assertEqual(len(self.fixture.definitions['functions']), 1)

    def test_get_function(self):
        self.fixture.add_function(self.test_function)
        function = self.fixture.get_function('test_function')
        self.assertEqual(function, self.test_function)

    def test_add_variable(self):
        self.fixture.add_variable(self.test_variable)
        self.assertEqual(len(self.fixture.definitions['variables']), 1)

    def test_get_variable(self):
        self.fixture.add_variable(self.test_variable)
        variable = self.fixture.get_variable('test_variable')
        self.assertEqual(variable, self.test_variable)

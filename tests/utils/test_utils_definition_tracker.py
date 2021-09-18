import unittest
from obscurepy.utils.definition_tracker import DefinitionTracker


class TestDefinitionTracker(unittest.TestCase):

    def setUp(self):
        self.fixture = DefinitionTracker.get_instance()
        self.fixture.clear_definitions()
        self.test_class = {
            'new_name': "NewClassName",
            'prev_name': "TestClass",
            'variables': [],
            'properties': [],
            'methods': {'some_method': {'new_name': 'obscured_method',
                                        'prev_name': 'some_method',
                                        'functions': {},
                                        'variables': [],
                                        'args': {'some_arg': {'new_name': 'obscured_arg',
                                                              'prev_name': 'some_arg'}},
                                        'return': ''}},
            'bases': []
        }
        self.test_function = {
            'new_name': "NewFunctionName",
            'prev_name': "TestFunction",
            'functions': {'some_function': {'new_name': 'obscured_function',
                                            'prev_name': 'some_function',
                                            'functions': {'nested_function': {'new_name': 'obscured_nested',
                                                                              'prev_name': 'nested_function',
                                                                              'functions': {},
                                                                              'variables': [],
                                                                              'args': [],
                                                                              'return': ''}},
                                            'variables': [],
                                            'args': [],
                                            'return': ''}},
            'variables': [],
            'args': [],
            'return': 'some_variable'
        }
        self.test_variable = {'prev_name': 'test_variable',
                              'new_name': 'new_test_variable'}

    def test_singleton(self):
        with self.assertRaises(Exception):
            DefinitionTracker()

    def test_get_nested_item(self):
        self.fixture.add_class(self.test_class)
        item = self.fixture.get_nested_item(
            'classes', 'methods', 'some_method')
        self.assertEqual(item['new_name'], 'obscured_method')

    def test_get_nested_item_none(self):
        self.fixture.add_class(self.test_class)
        item = self.fixture.get_nested_item(
            'classes', 'methods', 'different_method')
        self.assertEqual(item, None)

    def test_get_double_nested_item(self):
        self.fixture.add_function(self.test_function)
        item = self.fixture.get_double_nested_item(
            'functions', 'functions', 'functions', 'nested_function')
        self.assertEqual(item['new_name'], 'obscured_nested')

    def test_add_class(self):
        self.fixture.add_class(self.test_class)
        print(len(self.fixture.definitions['classes']))
        self.assertEqual(len(self.fixture.definitions['classes']), 1)

    def test_get_class(self):
        self.fixture.add_class(self.test_class)
        class_ = self.fixture.get_class("TestClass")
        self.assertEqual(class_['new_name'], "NewClassName")

    def test_get_nested_in_class(self):
        self.fixture.add_class(self.test_class)
        item = self.fixture.get_nested_in_class('methods', 'some_method')
        self.assertEqual(item['new_name'], 'obscured_method')

    def test_get_nested_in_class_none(self):
        self.fixture.add_class(self.test_class)
        item = self.fixture.get_nested_in_class('methods', 'different_method')
        self.assertEqual(item, None)

    def test_get_nested_in_class_method(self):
        self.fixture.add_class(self.test_class)
        item = self.fixture.get_nested_in_class_method('args', 'some_arg')
        self.assertEqual(item['new_name'], 'obscured_arg')

    def test_add_function(self):
        self.fixture.add_function(self.test_function)
        self.assertEqual(len(self.fixture.definitions['functions']), 1)

    def test_get_function(self):
        self.fixture.add_function(self.test_function)
        function = self.fixture.get_function("TestFunction")
        self.assertEqual(function['new_name'], "NewFunctionName")

    def test_get_nested_in_function(self):
        self.fixture.add_function(self.test_function)
        item = self.fixture.get_nested_in_function(
            'functions', 'some_function')
        self.assertEqual(item['new_name'], 'obscured_function')

    def test_get_double_nested_in_function(self):
        self.fixture.add_function(self.test_function)
        item = self.fixture.get_double_nested_in_function(
            'functions', 'nested_function')
        self.assertEqual(item['new_name'], 'obscured_nested')

    def test_add_variable(self):
        self.fixture.add_variable(self.test_variable)
        self.assertEqual(len(self.fixture.definitions['variables']), 1)

    def test_get_variable(self):
        self.fixture.add_variable(self.test_variable)
        variable = self.fixture.get_variable("test_variable")
        self.assertEqual(variable['new_name'], "new_test_variable")

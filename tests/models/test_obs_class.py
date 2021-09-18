import unittest
from obscurepy.models.obs_class import ObsClass
from obscurepy.models.obs_variable import ObsVariable
from obscurepy.models.obs_function import ObsFunction


class ObsClassTest(unittest.TestCase):

    def setUp(self):
        self.fixture = ObsClass('new name', 'old name', ('base1', 'base2'))

    def test_add_property(self):
        self.fixture.add_property(ObsVariable('new var1', 'old var1'))
        self.fixture.add_property(ObsVariable('new var1', 'old var1'))
        self.assertTrue(len(self.fixture.properties), 2)

    def test_add_property_non(self):
        with self.assertRaises(TypeError):
            self.fixture.add_property('a')

    def test_add_method(self):
        self.fixture.add_method(ObsFunction(
            'new func1', 'old func1', 'return val1'))
        self.fixture.add_method(ObsFunction(
            'new func1', 'old func1', 'return val2'))
        self.assertTrue(len(self.fixture.methods), 2)

    def test_add_method_non(self):
        with self.assertRaises(TypeError):
            self.fixture.add_method('a')

    def test_add_class(self):
        self.fixture.add_class(ObsClass('new func1', 'old func1', ('base1')))
        self.fixture.add_class(ObsClass('new func1', 'old func1', ('base2')))
        self.assertTrue(len(self.fixture.classes), 2)

    def test_add_class_non(self):
        with self.assertRaises(TypeError):
            self.fixture.add_class('a')

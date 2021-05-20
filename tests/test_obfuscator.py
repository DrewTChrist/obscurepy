import ast
import unittest
from obscurepy.obfuscator import Obfuscator
from obscurepy.handlers.class_handler import ClassHandler


class ObfuscatorTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Obfuscator()

    def tearDown(self):
        pass

    def test_build_chain(self):
        self.fixture.build_chain()
        self.assertEqual(type(self.fixture.chain), ClassHandler)

    def test_load_config(self):
        self.fixture.load_config()
        self.assertTrue(self.fixture.config is not None)
        self.assertEqual(self.fixture.config['test']['thisisatest'], 'yes')

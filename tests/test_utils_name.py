import unittest
from obscurepy.utils.name import *


class UtilsNameTest(unittest.TestCase):

    def setUp(self):
        self.string = 'test'

    def tearDown(self):
        pass

    def test_get_ascii_sum(self):
        self.assertEqual(get_ascii_sum(self.string), 448)

    def test_hex_name(self):
        self.assertEqual(hex_name(self.string), '_0x1c0')

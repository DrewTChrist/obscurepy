import unittest
from obscurepy.utils.log import *


class UtilsLogTest(unittest.TestCase):

    def test_get_verbose_logger(self):
        self.assertTrue(isinstance(
            get_verbose_logger(__name__), logging.Logger))

    def test_get_file_logger(self):
        self.assertTrue(isinstance(get_file_logger(__name__), logging.Logger))

import os
import unittest
from obscurepy.utils.log import *


class UtilsLogTest(unittest.TestCase):

    def setUp(self):
        self.logger = None

    def tearDown(self):
        self.logger = None

    def test_get_verbose_logger(self):
        self.logger = get_verbose_logger('verbose')
        self.assertTrue(isinstance(self.logger, logging.Logger))
        self.assertTrue(isinstance(
            self.logger.handlers[0], logging.StreamHandler))

    def test_get_file_logger(self):
        self.logger = get_file_logger('file')
        self.assertTrue(isinstance(self.logger, logging.Logger))
        self.assertTrue(isinstance(
            self.logger.handlers[0], logging.FileHandler))
        self.assertTrue(os.path.exists('obscurepy.log'))
        self.logger.handlers[0].close()
        os.remove('obscurepy.log')

    def test_get_null_logger(self):
        self.logger = get_null_logger('null')
        self.assertTrue(isinstance(self.logger, logging.Logger))
        self.assertTrue(isinstance(
            self.logger.handlers[0], logging.NullHandler))

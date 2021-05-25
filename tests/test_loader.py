import os
import unittest
from obscurepy.utils.loader import *


class TestTheLoader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_path = 'tests/test_data/test_files/'
        cls.files = os.listdir(cls.file_path)
        for i in range(len(cls.files)):
            cls.files[i] = cls.file_path + cls.files[i]

    def setUp(self):
        pass

    def test_load_file_none(self):
        with self.assertRaises(ValueError):
            text = load_file(None)

    def test_load_file_empty(self):
        with self.assertRaises(ValueError):
            text = load_file('')

    def test_load_file_bad(self):
        with self.assertRaises(OSError):
            text = load_file('notarealfile.txt')

    def test_load_file(self):
        text = load_file(self.files[0])
        self.assertTrue('this is test' in text)

    def test_load_files_none(self):
        with self.assertRaises(ValueError):
            texts = load_files(None)

    def test_load_files_empty(self):
        with self.assertRaises(ValueError):
            texts = load_files('')

    def test_load_files_bad(self):
        with self.assertRaises(OSError):
            texts = load_files(['notarealfile.txt'])

    def test_load_files(self):
        texts = load_files(self.files)
        self.assertEqual(len(texts), 3)

    def test_load_config_none(self):
        with self.assertRaises(ValueError):
            config = load_config(None)

    def test_load_config_empty(self):
        with self.assertRaises(ValueError):
            config = load_config('')

    def test_load_config_bad(self):
        with self.assertRaises(OSError):
            config = load_config('notarealfile.txt')

    def test_load_config(self):
        test_config = {'test': {'thisisatest': 'yes'}}
        config = load_config('tests/test_data/test_config.yaml')
        self.assertEqual(config, test_config)

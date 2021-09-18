import os
import unittest
from obscurepy.utils.loader import *
from obscurepy.handlers.classdef_handler import ClassDefHandler
import tests.plugins
import shutil


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

    def test_create_handlers(self):
        handlers = create_handlers(False, False)
        self.assertEqual(len(handlers), 8)

    def test_connect_handlers(self):
        handlers = create_handlers(False, False)
        chain = connect_handlers(handlers)
        self.assertEqual(type(chain), ClassDefHandler)

    def test_replace_handlers(self):
        handlers = create_handlers(False, False)
        new_handler = ClassDefHandler()
        new_handler.test_property = 42
        replace_handler(handlers, new_handler, False, False)
        self.assertEqual(handlers[0].test_property, 42)

    def test_load_custom_handlers(self):
        chain = load_custom_handlers('tests/plugins', False, False)
        self.assertEqual(
            type(chain), tests.plugins.classdef_handler.ClassDefHandler)

    def test_load_custom_handlers_missing(self):
        shutil.move('tests/plugins', 'tests/test_data')
        with self.assertRaises(Exception):
            chain = load_custom_handlers(False, False)
        shutil.move('tests/test_data/plugins', 'tests')

    def test_load_handlers(self):
        chain = load_handlers(False, False)
        self.assertEqual(type(chain), ClassDefHandler)

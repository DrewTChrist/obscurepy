import ast
import shutil
import os
from pathlib import Path
import unittest
from obscurepy.obfuscator import Obfuscator
from obscurepy.handlers.class_handler import ClassHandler


class ObfuscatorTest(unittest.TestCase):

    def setUp(self):
        self.fixture = Obfuscator('tests/my_module.py')
        self.fixture.filepath = None
        self.dynamic_fixture = None

    def tearDown(self):
        pass

    def test_constructor_multi_correct(self):
        self.dynamic_fixture = Obfuscator(
            is_project=True, project_directory="tests/test_project")

    def test_constructor_single_correct(self):
        self.dynamic_fixture = Obfuscator('tests/my_module.py')

    def test_constructor_incorrect(self):
        with self.assertRaises(Exception):
            self.dynamic_fixture = Obfuscator(
                filepath='tests/my_module.py', is_project=True)

    def test_build_chain(self):
        self.fixture.chain = None
        self.fixture.build_chain()
        self.assertEqual(type(self.fixture.chain), ClassHandler)

    def test_get_project_filepaths(self):
        self.fixture.project_directory = 'tests'
        self.fixture.get_project_filepaths()
        self.assertTrue('tests/test_obfuscator.py' in self.fixture.filepaths)

    def test_set_tree(self):
        self.fixture.tree = None
        self.fixture.set_tree('tests/my_module.py')
        self.assertEqual(type(self.fixture.tree), ast.Module)

    def test_build_output_directories_multi_file(self):
        self.fixture.project_directory = 'tests/test_data'
        self.fixture.output_directory = 'tests'
        self.fixture.is_project = True
        self.fixture.build_output_directories()
        self.assertTrue(os.path.exists('tests/obscurepy_out/test_data'))
        self.assertTrue(os.path.exists(
            'tests/obscurepy_out/test_data/test_files'))
        shutil.rmtree('tests/obscurepy_out')

    def test_build_output_directories_single_file(self):
        self.fixture.filepath = 'tests/my_module.py'
        self.fixture.output_directory = 'tests'
        self.fixture.build_output_directories()
        self.assertTrue(os.path.exists('tests/obscurepy_out'))
        os.rmdir('tests/obscurepy_out')

    def test_write_tree_to_file(self):
        self.fixture.set_tree('tests/my_module.py')
        self.fixture.write_tree_to_file('tests/obfuscated.py')
        self.assertTrue(Path('tests/obfuscated.py').exists())
        os.remove('tests/obfuscated.py')

    def test_obscure_multi_file(self):
        self.fixture.is_project = True
        self.fixture.project_directory = 'tests/test_project'
        self.fixture.output_directory = 'tests'
        self.fixture.obscure()
        self.assertTrue(os.path.exists('tests/obscurepy_out/test_project'))
        self.assertTrue(os.path.exists(
            'tests/obscurepy_out/test_project/my_module.py'))
        self.assertTrue(os.path.exists(
            'tests/obscurepy_out/test_project/another_module.py'))
        shutil.rmtree('tests/obscurepy_out')

    def test_obscure_single_file(self):
        self.fixture.filepath = 'tests/my_module.py'
        self.fixture.output_directory = 'tests'
        self.fixture.obscure()
        self.assertTrue(os.path.exists('tests/obscurepy_out/my_module.py'))
        shutil.rmtree('tests/obscurepy_out')

    def test_obscure_file(self):
        self.fixture.filepath = 'tests/my_module.py'
        self.fixture.output_directory = 'tests'
        self.fixture.obscure_file()
        self.assertTrue(os.path.exists('tests/obscurepy_out/my_module.py'))
        shutil.rmtree('tests/obscurepy_out')

    def test_obscure_project(self):
        self.fixture.is_project = True
        self.fixture.project_directory = 'tests/test_project'
        self.fixture.output_directory = 'tests'
        self.fixture.obscure_project()
        self.assertTrue(os.path.exists('tests/obscurepy_out/test_project'))
        self.assertTrue(os.path.exists(
            'tests/obscurepy_out/test_project/my_module.py'))
        self.assertTrue(os.path.exists(
            'tests/obscurepy_out/test_project/another_module.py'))
        shutil.rmtree('tests/obscurepy_out')

    def test_is_multi_file_correct(self):
        self.fixture.is_project = True
        self.fixture.project_directory = 'tests/test_data'
        self.assertTrue(self.fixture.is_multi_file())

    def test_is_multi_file_incorrect(self):
        self.assertFalse(self.fixture.is_multi_file())

    def test_is_single_file_correct(self):
        self.fixture.filepath = 'tests/test_obfuscator.py'
        self.assertTrue(self.fixture.is_single_file())

    def test_is_single_file_incorrect(self):
        self.fixture.is_project = True
        self.assertFalse(self.fixture.is_single_file())

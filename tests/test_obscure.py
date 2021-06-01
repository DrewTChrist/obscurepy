import os
import unittest
from click.testing import CliRunner
from obscurepy.scripts.obscure import obscure


class ObscureTest(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.source1 = 'class FirstClass:\n\tpass\n\n' \
                       'class SecondClass:\n\tpass\n\n' \
                       'def FirstFunction():\n\tc = "a literal"\n\n' \
                       'def SecondFunction():\n\tpass\n\n' \
                       'a = FirstClass()\n\n' \
                       'b = SecondClass()\n\n' \
                       'FirstFunction()\n\n' \
                       'SecondFunction()\n\n' \
                       'a = SecondClass()\n\n' \
                       'c = 42'
        self.source2 = 'class ThirdClass:\n\t' \
                       'pass\n\n' \
                       'def ThirdFunction():\n\t' \
                       'c = 42.0'

    def create_test_project(self):
        os.mkdir('test_project')
        os.mkdir('test_project/some_package')
        with open('test_project/__init__.py', 'w') as fp:
            fp.close()
        with open('test_project/some_package/__init__.py', 'w') as fp:
            fp.close()
        with open('test_project/first_module.py', 'w') as fp:
            fp.write(self.source1)
            fp.close()
        with open('test_project/some_package/second_module.py', 'w') as fp:
            fp.write(self.source2)
            fp.close()

    def create_test_file(self):
        with open('my_module.py', 'w') as file:
            file.write(self.source1)
            file.close()

    def test_obscure_single_file(self):
        with self.runner.isolated_filesystem():
            self.create_test_file()
            result = self.runner.invoke(obscure, ['--filepath=my_module.py'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.exists('obscurepy_out/my_module.py'))

    def test_obscure_multi_file(self):
        with self.runner.isolated_filesystem():
            self.create_test_project()
            result = self.runner.invoke(
                obscure, ['-p', '--project_dir=test_project'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.exists(
                'obscurepy_out/test_project/first_module.py'))
            self.assertTrue(os.path.exists(
                'obscurepy_out/test_project/some_package/second_module.py'))

    def test_obscure_filepath_and_project(self):
        result = self.runner.invoke(obscure, ['--filepath=my_module.py', '-p'])
        self.assertTrue(result.exit_code > 0)

    def test_obscure_filepath_and_projectdir(self):
        result = self.runner.invoke(
            obscure, ['--filepath=my_module.py', '--project_dir=test_project'])
        self.assertTrue(result.exit_code > 0)

    def test_obscure_project_not_projectdir(self):
        result = self.runner.invoke(obscure, ['-p'])
        self.assertTrue(result.exit_code > 0)

    def test_obscure_notproject_and_projectdir(self):
        result = self.runner.invoke(obscure, ['--project_dir=test_project'])
        self.assertTrue(result.exit_code > 0)

    def test_obscure_no_args(self):
        result = self.runner.invoke(obscure, [])
        self.assertTrue(result.exit_code > 0)

    def test_obscure_file_logging(self):
        with self.runner.isolated_filesystem():
            self.create_test_file()
            result = self.runner.invoke(
                obscure, ['--filepath=my_module.py', '-l'])
            self.assertEqual(result.exit_code, 0)
            self.assertTrue(os.path.exists('obscurepy.log'))

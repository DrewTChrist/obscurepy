import ast
import astunparse
import os
import sys
from obscurepy.utils.loader import load_handlers, load_file
from obscurepy.utils.tree import add_parents
from obscurepy.utils.log import get_verbose_logger, get_file_logger, get_null_logger


class Obfuscator:
    """Main obfuscator class for managing files, handlers and other processes

    Attributes:
        **filepath (str)**: Single file to be obscured

        **is_project (bool)**: Boolean representing whether or not to try obscuring a multi file project

        **project_directory (str)**: The directory of the project to be obscured

        **output_directory (str)**: The directory to output the obscured code

        **filepaths (list)**: List of filenames to be obscured

        **chain (:obj: `Handler`)**: A single handler which is the first in the chain of handlers

        **tree (:obj: `ast.Module`)**: Reference to the ast tree created from text attribute

    Args:
        **filepath (str)**: Single file to be obscured

        **is_project (bool)**: Boolean representing whether or not to try obscuring a multi file project

        **project_directory (str)**: The directory of the project to be obscured

        **output_directory (str)**: The directory to output the obscured code
    """

    def __init__(self, filepath=None, is_project=False, project_directory=None,
                 output_directory='.', log=False, verbose=False):
        """Creates an instance of an Obfuscator"""
        self.filepath = filepath
        self.is_project = is_project
        self.project_directory = project_directory
        self.output_directory = output_directory
        self.filepaths = []
        self.chain = None
        self.tree = None
        self.log = log
        self.verbose = verbose
        self.logger = None

        self.setup_logging()

        self.build_chain()

        if not self.is_multi_file() and not self.is_single_file():
            raise Exception(
                'Improper configuration for both single file and projects')

    def setup_logging(self):
        """Sets the Obfuscator logger based on user configuration"""
        if not self.log:
            self.logger = get_null_logger(self.__class__.__name__)
        elif self.verbose:
            self.logger = get_verbose_logger(self.__class__.__name__)
        else:
            self.logger = get_file_logger(self.__class__.__name__)

    def build_chain(self):
        """Loads handlers and assigns the first one to the chain property"""
        self.logger.info('Building handlers chain')
        self.chain = load_handlers(self.log, self.verbose)

    def get_project_filepaths(self):
        """Sets the filepaths property to a list of filepaths found in the project directory"""
        self.logger.info('Getting project file paths')
        filepaths = []
        for dp, dn, filenames in os.walk(self.project_directory):
            if '__pycache__' in dn:
                dn.remove('__pycache__')
            for f in filenames:
                filepaths.append(os.path.join(dp, f))
        self.filepaths = filepaths

    def set_tree(self, filepath):
        """Sets the tree property to the parsed abstract syntax tree of source in the filepath provided

        Args:
            **filepath (str)**: File path of which to get the tree
        """
        self.logger.info('Setting the tree')
        text = load_file(filepath)
        self.tree = ast.parse(text)
        add_parents(self.tree)

    def build_output_directories(self):
        """Recreates the project directory structure in the output directory"""
        self.logger.info('Building output directories')
        if self.is_multi_file():
            os.mkdir(os.path.join(self.output_directory, 'obscurepy_out'))
            directories = []
            for dp, dn, filenames in os.walk(self.project_directory):
                if '__pycache__' not in dp:
                    directories.append(dp)
            for directory in directories:
                if self.output_directory in directory:
                    os.mkdir(os.path.join(self.output_directory,
                                          'obscurepy_out',
                                          directory.replace(f"{self.output_directory}/", "")))
                else:
                    os.mkdir(os.path.join(self.output_directory,
                             'obscurepy_out', directory))
        elif self.is_single_file():
            os.mkdir(os.path.join(self.output_directory, 'obscurepy_out'))

    def write_tree_to_file(self, filepath):
        """Writes unparsed abstract syntax trees to files

        Args:
            **filepath (str)**: The location to save the source of the ast
        """
        self.logger.info('Writing tree to file')
        if sys.version_info < (3, 9):
            text = astunparse.unparse(self.tree)
        else:
            text = ast.unparse(self.tree)
        with open(filepath, 'w') as file:
            file.write(text)
            file.close()

    def obscure(self):
        """Obscures the project or single file as defined in the class properties"""
        self.logger.info('Obscuring')
        if self.is_multi_file():
            self.obscure_project()
        elif self.is_single_file():
            self.obscure_file()

    def obscure_file(self):
        """Obscures a single file"""
        self.logger.info('Obscuring single file')
        self.set_tree(self.filepath)
        self.tree = self.chain.handle(self.tree)
        self.build_output_directories()
        if self.output_directory in self.filepath:
            self.write_tree_to_file(os.path.join(self.output_directory,
                                                 'obscurepy_out',
                                                 self.filepath.replace(f"{self.output_directory}/", "")))
        else:
            self.write_tree_to_file(os.path.join(
                self.output_directory, 'obscurepy_out', self.filepath))

    def obscure_project(self):
        """Obscures a multi file project"""
        self.logger.info('Obscuring project')
        self.get_project_filepaths()
        self.build_output_directories()
        for filepath in self.filepaths:
            self.set_tree(filepath)
            self.tree = self.chain.handle(self.tree)
            if self.output_directory in filepath:
                self.write_tree_to_file(os.path.join(self.output_directory,
                                                     'obscurepy_out',
                                                     filepath.replace(f"{self.output_directory}/", "")))
            else:
                self.write_tree_to_file(os.path.join(
                    self.output_directory, 'obscurepy_out', filepath))

    def is_multi_file(self):
        """Checks if this class is configured properly for a multi file project"""
        return self.is_project and self.project_directory and os.path.exists(self.project_directory)

    def is_single_file(self):
        """Checks if this class is configured properly for a single file"""
        return not self.is_project and self.filepath and os.path.exists(self.filepath)

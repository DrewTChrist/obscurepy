from abc import ABC
import ast
from obscurepy.utils.tree import add_parents
from obscurepy.utils.log import get_verbose_logger, get_file_logger, get_null_logger


class Handler(ABC, ast.NodeTransformer):
    """Abstract Handler class that inherits from ast.NodeTransformer

    Attributes:
        **next (:obj: `Handler`)**: The next handler to be executed

        **_debug_name (str)**: Class name used for debugging purposes

        **execution_priority (int)**: Value used to determine when a handler should be executed
    """

    def __init__(self, log, verbose):
        """Defines attributes necessary for sub classes"""
        self.next = None
        self.execution_priority = 0
        self.log = log
        self.verbose = verbose
        self.logger = None
        self.setup_logging()

    def setup_logging(self):
        if not self.log:
            self.logger = get_null_logger(self.__class__.__name__)
        elif self.verbose:
            self.logger = get_verbose_logger(self.__class__.__name__)
        else:
            self.logger = get_file_logger(self.__class__.__name__)

    def set_next(self, next_handler):
        """Sets the next handler to be executed after the current

        Args:
            **next_handler (:ob: `Handler`)**: Handler to be set as the next
        """
        self.next = next_handler

    def get_next(self):
        """Gets whichever handler is currently set as next

        Returns:
            Handler if next is set, None if next is None
        """
        return self.next

    def handle(self, tree):
        """Executes the visit method inherited from ast.NodeTransformer and calls handle on the next handler

        Args:
            **tree (:obj: `ast.Module`)**: A root ast node

        Returns:
            The modified tree
        """
        self.logger.info('Handling tree')
        tree = self.visit(tree)
        add_parents(tree)

        if self.next is not None:
            return self.next.handle(tree)

        return tree

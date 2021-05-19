from abc import ABC
import ast


class Handler(ABC, ast.NodeTransformer):
    """Abstract Handler class that inherits from ast.NodeTransformer

    Attributes:
        **next (:obj: `Handler`)**: The next handler to be executed

        **_debug_name (str)**: Class name used for debugging purposes

        **execution_priority (int)**: Value used to determine when a handler should be executed
    """

    def __init__(self):
        """Defines attributes necessary for sub classes"""
        self.next = None
        self._debug_name = ''
        self.execution_priority = 0

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
        tree = self.visit(tree)

        if self.next is not None:
            return self.next.handle(tree)

        return tree

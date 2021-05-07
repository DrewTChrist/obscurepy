from abc import ABC
import ast


class Handler(ABC, ast.NodeTransformer):
    """Abstract Handler class"""

    def __init__(self):
        self.next = None

    def set_next(self, next_handler):
        self.next = next_handler

    def get_next(self):
        return self.next

    def handle(self, tree):
        tree = self.visit(tree)

        if self.next is not None:
            return self.next.handle(tree)

        return tree

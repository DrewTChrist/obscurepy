import ast
import pprint
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


def handle_args(node, tracker):
    if tracker.get_nested_in_function('args', node.arg):
        node.arg = tracker.get_nested_in_function('args', node.arg)['new_name']
    elif tracker.get_nested_in_class_method('args', node.arg)['new_name']:
        node.arg = tracker.get_nested_in_class_method('args', node.arg)[
            'new_name']

    return node


class ArgHandler(Handler):
    """Class to traverse and modify arg nodes in an ast

    Attributes:
        **execution_priority (int)**: Used to determine when ArgHandler should be executed
    """

    def __init__(self, log=False, verbose=False):
        """Creates a new instance of an ArgHandler"""
        super(ArgHandler, self).__init__(log, verbose)
        self.execution_priority = 8

    def visit_arg(self, node):
        """Overrides the NodeTransformer visit_arg method. This method makes modifications
           to arg nodes in an abstract syntax tree

        Args:
            **node (:obj: `ast.Assign`)**: The current arg node to be modified

        Returns:
            The modified arg node
        """
        self.logger.info('visit_arg')
        tracker = DefinitionTracker.get_instance()
        node = handle_args(node, tracker)
        return node

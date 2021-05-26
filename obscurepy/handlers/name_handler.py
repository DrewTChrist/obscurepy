import ast
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.treeutils.class_scope_utils import *
from obscurepy.treeutils.function_scope_utils import *


def obscure_class_bases(node, tracker):
    """Obscures the Name nodes of a ClassDef node

    Args:
        **node (:obj: `ast.Name`)**: Current node to be obscured

        **tracker (:obj: `DefinitionTracker`)**: The instance of the definition tracker for checking if bases exist

    Returns:
        The obscured ast.Name node if it is the child of a ClassDef node, otherwise it is not obscured
    """
    if type(node.parent) == ast.ClassDef and node in node.parent.bases:
        if node.id in tracker.definitions['classes']:
            node.id = tracker.definitions['classes'][node.id]['new_name']

    return node


def handle_function_scope(node, tracker):
    """Internal method for handling names within the scope of a function

    Args:
        **node (:obj: `ast.Name`)**: Current Name node
    """
    if is_in_function_scope(node):
        if node.id in tracker.definitions['functions']['variables']:
            node.id = tracker.definitions['functions']['variables'][node.id]

    return node


def handle_global_scope(node, tracker):
    """Internal method for handling names within the global scope

    Args:
        **node (:obj: `ast.Name`)**: Current Name  node
    """
    if not is_in_function_scope(node) and not is_in_class_scope(node):
        if node.id in tracker.definitions['variables']:
            node.id = tracker.definitions['variables'][node.id]

    return node


def handle_class_scope(node, tracker):
    """Internal method for handling names within the scope of a class

    Args:
        **node (:obj: `ast.Name`)**: Current Name node
    """
    if is_in_class_scope(node):
        if node.id in tracker.definitions['classes']['variables']:
            node.id = tracker.definitions['classes']['variables'][node.id]

    return node


class NameHandler(Handler):
    """Class to traverse and modify Name nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when NameHandler should be executed
    """

    def __init__(self):
        """Creates a new instance of a NameHandler"""
        super(NameHandler, self).__init__()
        self._debug_name = 'NameHandler'
        self.execution_priority = 6

    def visit_Name(self, node):
        """Overrides the NodeTransformer visit_Name method. This method makes modifications
           to the abstract syntax tree  when it encounters a Name node

           Args:
               **node (:obj: `ast.Name`)**: The current Name node to be modified

            Returns:
                The modified Name node
        """
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.id, str):
            node = obscure_class_bases(node, tracker)
            #node = handle_global_scope(node, tracker)
            #node = handle_class_scope(node, tracker)
            #node = handle_function_scope(node, tracker)

        return node

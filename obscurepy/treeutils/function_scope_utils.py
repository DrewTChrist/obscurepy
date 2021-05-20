import ast
from obscurepy.treeutils.general import *


def is_in_function_scope(node):
    """Checks if a node is within the scope of a function

    Args:
        **node (:obj:)**: node for which to check the scope

    Returns:
        True if the node is within the scope of a function, False otherwise
    """
    return has_parent_of_type(node, ast.FunctionDef)


def get_parent_function_name(node):
    """Gets the name of the parent node if it is a function

    Args:
        **node (:obj:)**: node of which to get the parent function name

    Returns:
        The name of the parent function if node is within the scope of a function

    Raises:
        Exception if the node is not within the scope of a function
    """
    if is_in_function_scope(node):
        return node.parent.name
    else:
        raise Exception("This node is not within the scope of a function")

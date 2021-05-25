import ast
from obscurepy.treeutils.general import *


def is_in_class_scope(node):
    """Checks if a node is within the scope of a class

    Args:
        **node (:obj:)**: node for which to check the scope

    Returns:
        True if the node is within the scope of a class, False otherwise
    """
    return has_parent_of_type(node, ast.ClassDef)


def get_parent_class_name(node):
    """Gets the name of the parent node if it is a class

    Args:
        **node (:obj:)**: node of which to get the parent class name

    Returns:
        The name of the parent class if node is within the scope of a class

    Raises:
        Exception if the node is not within the scope of a class
    """
    if is_in_class_scope(node):
        return node.parent.name
    else:
        raise Exception("This node is not within a class scope")

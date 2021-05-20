import ast


def add_parents(root):
    """Helper function to add parent property to ast tree nodes
       Credit goes to this answer here: https://stackoverflow.com/a/43311383

    Args:
        **root (:obj: `ast.Module`)**: Top level ast node
    """
    for node in ast.walk(root):
        for child in ast.iter_child_nodes(node):
            child.parent = node


def get_node_type(node):
    """Simply gets the type of an ast node

    Args:
        **node (:obj:)**: ast node

    Returns:
        The type of an ast node

    """
    return type(node)


def has_parent_of_type(node, type_):
    """Simply checks if the parent of a node is of a certain type

    Args:
        **node (:obj:)**: an ast node

        **type_ (type)**: the type to check the node against

    Returns:
        True if node is of type type_, False otherwise
    """
    return get_node_type(node.parent) == type_

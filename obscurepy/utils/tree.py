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

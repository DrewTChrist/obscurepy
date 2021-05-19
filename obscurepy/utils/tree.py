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

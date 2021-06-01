import ast
from obscurepy.handlers.handler import Handler


def handle_str(node):
    """Replaces an ast.Constant containing a string, with an ascii representation joined together

    Args:
        **node (:obj: `ast.Constant`)**: The node to replace with the ast.Call node

    Returns:
        A new obscured node with updated locations
    """
    new_node = ast.Call(
        func=ast.Attribute(
            value=ast.Constant(value='', kind=None),
            attr='join',
            ctx=ast.Load(),
        ),
        args=[
            ast.ListComp(
                elt=ast.Call(
                    func=ast.Name(id='chr', ctx=ast.Load()),
                    args=[ast.Name(id='x', ctx=ast.Load())],
                    keywords=[]
                ),
                generators=[
                    ast.comprehension(
                        target=ast.Name(id='x', ctx=ast.Store()),
                        iter=ast.List(
                            elts=[
                                ast.Constant(value=ord(x), kind=None) for x in node.value
                            ],
                            ctx=ast.Load(),
                        ),
                        ifs=[],
                        is_async=0,
                    ),
                ],
            ),
        ],
        keywords=[]
    )
    return ast.copy_location(new_node, node)


def handle_int(node):
    """Replaces an ast.Constant containing an integer with a hex representation converted back to int

    Args:
        **node (:obj: `ast.Constant`)**: The node to replace with the ast.Call node

    Returns:
        A new obscured node with updated locations
    """
    new_node = ast.Call(
        func=ast.Name(id='int', ctx=ast.Load()),
        args=[ast.Constant(value=hex(node.value)), ast.Constant(value=16)],
        keywords=[],
    )
    return ast.copy_location(new_node, node)


def handle_float(node):
    """Replaces an ast.Constant containing an float with a hex representation converted back to float

    Args:
        **node (:obj: `ast.Constant`)**: The node to replace with the ast.Call node

    Returns:
        A new obscured node with updated locations
    """
    new_node = ast.Call(
        func=ast.Name(id='float.fromhex', ctx=ast.Load()),
        args=[ast.Constant(value=float.hex(node.value))],
        keywords=[],
    )
    return ast.copy_location(new_node, node)


def handle_constant_types(node):
    """This function properly directs each node to the function that handles its specific type

    Args:
        **node (:obj: `ast.Constant`)**: The node to be obscured

    Return:
        The obscured node
    """
    if isinstance(node.value, str):
        node = handle_str(node)
    elif isinstance(node.value, int):
        node = handle_int(node)
    elif isinstance(node.value, float):
        node = handle_float(node)

    return node


class ConstantHandler(Handler):
    """Class to traverse and modify Constant nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when ConstantHandler should be executed
    """

    def __init__(self, log=False, verbose=False):
        """Creates a new instance of a ConstantHandler"""
        super(ConstantHandler, self).__init__(log, verbose)
        self.execution_priority = 7

    def visit_Constant(self, node):
        """Overrides the NodeTransformer visit_Constant method and obscures Constants

           Args:
               **node (:obj: `ast.Constant`)**: The current Constant node to be modified

            Returns:
                The obscured node
        """
        self.logger.info('visit_Constant')
        return handle_constant_types(node)

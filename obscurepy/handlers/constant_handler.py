import ast
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


def handle_str(node):
    # obscure string literal
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
    # obscure int
    new_node = ast.Call(
        func=ast.Name(id='int', ctx=ast.Load()),
        args=[ast.Constant(value=hex(node.value)), ast.Constant(value=16)],
        keywords=[],
    )
    return ast.copy_location(new_node, node)


def handle_float(node):
    # obscure float
    return node


def handle_constant_types(node):
    if isinstance(node.value, str):
        node = handle_str(node)
    elif isinstance(node.value, int):
        node = handle_int(node)
    elif isinstance(node.value, float):
        node = handle_float(node)

    return node


class ConstantHandler(Handler):

    def __init__(self):
        super(ConstantHandler, self).__init__()
        self._debug_name = 'StrHandler'
        self.execution_priority = 7

    def visit_Constant(self, node):
        tracker = DefinitionTracker.get_instance()
        node = handle_constant_types(node)
        return node

from obscurepy.handlers.handler import Handler
import ast


class StringLiteralHandler(Handler):

    def __init__(self):
        super(StringLiteralHandler, self).__init__()

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            node.name = "Hello"
        return node

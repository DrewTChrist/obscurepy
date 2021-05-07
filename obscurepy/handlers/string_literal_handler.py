from obscurepy.handlers.handler import Handler


class StringLiteralHandler(Handler):

    def __init__(self):
        super(StringLiteralHandler, self).__init__()

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            node.name = "Hello"
        return node

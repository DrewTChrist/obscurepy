from obscurepy.handlers.handler import Handler


class FunctionHandler(Handler):

    def __init__(self):
        super(FunctionHandler, self).__init__()

    def visit_FunctionDef(self, node):
        if isinstance(node.name, str):
            node.name = "HelloFunction"
        return node

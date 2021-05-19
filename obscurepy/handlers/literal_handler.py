from obscurepy.handlers.handler import Handler


class LiteralHandler(Handler):
    """StringLiteralHandler class"""

    def __init__(self):
        super(LiteralHandler, self).__init__()
        self._debug_name = "LiteralHandler"
        self.execution_priority = 4

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            node.name = "Hello"
        return node

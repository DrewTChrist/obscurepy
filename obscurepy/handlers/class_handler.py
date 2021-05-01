from obscurepy.handlers.handler import Handler
import ast


class ClassHandler(Handler):

    def __init__(self):
        super(ClassHandler, self).__init__()

    def visit_ClassDef(self, node):
        if isinstance(node.name, str):
            node.name = "Hello"
        return node

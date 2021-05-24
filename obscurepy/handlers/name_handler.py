from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.treeutils.class_scope_utils import *


def obscure_class_bases(node):
    pass


class NameHandler(Handler):

    def __init__(self):
        super(NameHandler, self).__init__()
        self._debug_name = 'NameHandler'
        self.execution_priority = 6

    def visit_Name(self, node):
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.id, str):
            obscure_class_bases(node)

        return node

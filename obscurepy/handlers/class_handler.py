from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


class ClassHandler(Handler):
    """ClassHandler class"""

    def __init__(self):
        super(ClassHandler, self).__init__()

    def visit_ClassDef(self, node):
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.name, str):
            node_dict = tracker.add_class(node.name)
            node.name = node_dict['name']
        return node

from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


class CallHandler(Handler):
    """Class to traverse and modify Call nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes
        **execution_priority (int)**: Used to determine when CallHandler should be executed
    """

    def __init__(self):
        """Creates a new instance of a CallHandler"""
        super(CallHandler, self).__init__()
        self._debug_name = 'CallHandler'
        self.execution_priority = 3

    def visit_Call(self, node):
        """Overrides the NodeTransformer visit_Call method. This method makes modifications
           to the abstract syntax tree and stores assignments with the DefinitionTracker class

        Args:
            **node (:obj: `ast.Call`)**: The current Call node to be modified
        """
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.func.id, str):
            if node.func.id in tracker.definitions['classes']:
                node.func.id = tracker.definitions['classes'][node.func.id]['new_name']
            elif node.func.id in tracker.definitions['functions']:
                node.func.id = tracker.definitions['functions'][node.func.id]['new_name']
        return node

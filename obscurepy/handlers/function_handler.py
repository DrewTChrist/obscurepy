from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


class FunctionHandler(Handler):
    """Class to traverse and modify FunctionDef nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when FunctionHandler should be executed
    """

    def __init__(self):
        """Creates a new instance of a FunctionHandler"""
        super(FunctionHandler, self).__init__()
        self._debug_name = 'FunctionDefHandler'
        self.execution_priority = 2

    def visit_FunctionDef(self, node):
        """Overrides the NodeTransformer visit_FunctionDef method. This method makes modifications
           to the abstract syntax tree and stores assignments with the DefinitionTracker class

        Args:
            **node (:obj: `ast.FunctionDef`)**: The current FunctionDef node to be modified

        Returns:
            The modified FunctionDef node
        """
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.name, str):
            previous_name = node.name
            tracker.add_function(node.name)
            node.name = tracker.definitions['functions'][previous_name]
        return node

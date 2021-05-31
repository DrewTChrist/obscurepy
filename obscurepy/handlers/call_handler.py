from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


class CallHandler(Handler):
    """Class to traverse and modify Call nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes
        **execution_priority (int)**: Used to determine when CallHandler should be executed
    """

    def __init__(self, log=False, verbose=False):
        """Creates a new instance of a CallHandler"""
        super(CallHandler, self).__init__(log, verbose)
        self.execution_priority = 3

    def visit_Call(self, node):
        """Overrides the NodeTransformer visit_Call method. This method makes modifications
           to the abstract syntax tree and stores assignments with the DefinitionTracker class

        Args:
            **node (:obj: `ast.Call`)**: The current Call node to be modified
        """
        self.logger.info('visit_Call')
        tracker = DefinitionTracker.get_instance()
        return node

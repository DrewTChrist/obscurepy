from obscurepy.handlers.handler import Handler


class AssignHandler(Handler):
    """Class to traverse and modify Assign nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when AssignHandler should be executed
    """

    def __init__(self, log=False, verbose=False):
        """Creates a new instance of an AssignHandler"""
        super(AssignHandler, self).__init__(log, verbose)
        self.execution_priority = 5

    def visit_Assign(self, node):
        """Overrides the NodeTransformer visit_Assign method. This method makes modifications
           to the abstract syntax tree and stores assignments with the DefinitionTracker class

        Args:
            **node (:obj: `ast.Assign`)**: The current Assign node to be modified

        Returns:
            The modified Assign node
        """
        self.logger.info('visit_Assign')
        return node

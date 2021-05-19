from ast import FunctionDef, ClassDef
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


class AssignHandler(Handler):
    """Class to traverse and modify Assign nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when AssignHandler should be executed
    """

    def __init__(self):
        """Creates a new instance of an AssignHandler"""
        super(AssignHandler, self).__init__()
        self._debug_name = 'AssignHandler'
        self.execution_priority = 5

    def visit_Assign(self, node):
        """Overrides the NodeTransformer visit_Assign method. This method makes modifications
           to the abstract syntax tree and stores assignments with the DefinitionTracker class

        Args:
            **node (:obj: `ast.Assign`)**: The current Assign node to be modified

        Returns:
            The modified Assign node
        """
        tracker = DefinitionTracker.get_instance()
        for i in range(len(node.targets)):
            if isinstance(node.targets[i].id, str):
                previous_name = node.targets[i].id
                if node.targets[i].id not in tracker.definitions['variables']:
                    tracker.add_variable(node.targets[i].id)
                node.targets[i].id = tracker.definitions['variables'][previous_name]
        return node

    def _handle_function_scope_assignments(self, node):
        """Internal method for handling assignments within the scope of a function
        Args:
            **node (:obj: `ast.Assign`)**: Current Assign node
        """
        pass

    def _handle_global_scope_assignments(self, node):
        """Internal method for handling assignments within the global scope
        Args:
            **node (:obj: `ast.Assign`)**: Current Assign node
        """
        pass

    def _handle_class_scope_assignments(self, node):
        """Internal method for handling assignments within the scope of a class
        Args:
            **node (:obj: `ast.Assign`)**: Current Assign node
        """
        pass

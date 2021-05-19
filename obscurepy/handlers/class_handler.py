from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


class ClassHandler(Handler):
    """Class to traverse and modify ClassDef nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when ClassHandler should be executed
    """

    def __init__(self):
        """Creates a new instance of a ClassHandler"""
        super(ClassHandler, self).__init__()
        self._debug_name = 'ClassDefHandler'
        self.execution_priority = 1

    def visit_ClassDef(self, node):
        """Overrides the NodeTransformer visit_ClassDef method. This method makes modifications
           to the abstract syntax tree and stores class definitions with the DefinitionTracker class

           Args:
               **node (:obj: `ast.ClassDef`)**: The current ClassDef node to be modified

            Returns:
                The modified ClassDef node
        """
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.name, str):
            previous_name = node.name
            tracker.add_class(node.name)
            node.name = tracker.definitions['classes'][previous_name]
        return node

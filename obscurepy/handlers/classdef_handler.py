import ast

from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


class ClassDefHandler(Handler):
    """Class to traverse and modify ClassDef nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when ClassHandler should be executed
    """

    def __init__(self):
        """Creates a new instance of a ClassHandler"""
        super(ClassDefHandler, self).__init__()
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
            class_dict = self._create_class_dictionary(node)
            tracker.add_class(class_dict)
            node.name = tracker.definitions['classes'][node.name]['new_name']
        return node

    def _create_class_dictionary(self, node):
        class_dict = {
            'new_name': "",
            'prev_name': node.name,
            'variables': self._get_variables(node),
            'properties': self._get_properties(node),
            'methods': self._get_methods(node),
            'bases': self._get_base_classes(node)
        }
        return class_dict

    def _get_variables(self, node):
        """An ugly function that gets a list of class variables

        Args:
            **node (:obj: `ast.ClassDef`)**: The ClassDef node for which to get the variables of

        Returns:
            List of class variables (str), or empty list if none
        """
        variables = []
        for variable in node.body:
            if type(variable) == ast.Assign:
                for target in variable.targets:
                    if type(target) == ast.Name:
                        variables.append(target.id)
        return variables

    def _get_properties(self, node):
        """An ugly function that gets a list of class properties

        Args:
            **node (:obj: `ast.ClassDef`)**: The ClassDef node for which to get the properties of

        Returns:
            List of class properties (str), or empty list if none
        """
        properties = []
        for method in node.body:
            if type(method) == ast.FunctionDef:
                if method.name == '__init__':
                    for assign in method.body:
                        if type(assign) == ast.Assign:
                            for target in assign.targets:
                                if target.value.id == 'self':
                                    properties.append(target.attr)
        return properties

    def _get_methods(self, node):
        """An ugly function that gets a list of class methods

        Args:
            **node (:obj: `ast.ClassDef`)**: The ClassDef node for which to get the methods of

        Returns:
            List of class methods (str), or empty list if none
        """
        methods = []
        for method in node.body:
            if type(method) == ast.FunctionDef:
                methods.append(method.name)
        return methods

    def _get_base_classes(self, node):
        """An ugly function that gets a list of classes inhereted from

        Args:
            **node (:obj: `ast.ClassDef`)**: The ClassDef node for which to get the base classes of

        Returns:
            List of base classes (str), or empty list if none
        """
        bases = []
        for base in node.bases:
            bases.append(base.id)
        return bases

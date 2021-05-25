import ast

from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


def get_base_classes(node):
    """An ugly function that gets a list of classes inhereted from

    Args:
        **node (:obj: `ast.ClassDef`)**: The ClassDef node for which to get the base classes of

    Returns:
        List of base classes (str), or empty list if none
    """
    bases = []
    if type(node) == ast.ClassDef:
        for base in node.bases:
            bases.append(base.id)
    return bases


def get_methods(node):
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


def get_properties(node):
    """An ugly function that gets a list of class properties

    Args:
        **node (:obj: `ast.ClassDef`)**: The ClassDef node for which to get the properties of

    Returns:
        List of class properties (str), or empty list if none
    """
    properties = []
    for method in node.body:
        if type(method) == ast.FunctionDef:
            # This needs to check for all 'self' properties no just those in __init__
            if method.name == '__init__':
                for assign in method.body:
                    if type(assign) == ast.Assign:
                        for target in assign.targets:
                            if target.value.id == 'self':
                                properties.append(target.attr)
    return properties


def get_variables(node):
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


def create_class_dictionary(node):
    class_dict = {
        'new_name': "",
        'prev_name': node.name,
        'variables': get_variables(node),
        'properties': get_properties(node),
        'methods': get_methods(node),
        'bases': get_base_classes(node)
    }
    return class_dict


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
        # Check to make sure this node is not already in tracker definitions
        if isinstance(node.name, str):
            class_dict = create_class_dictionary(node)
            tracker.add_class(class_dict)
            node.name = tracker.definitions['classes'][node.name]['new_name']
        return node

import ast
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.tree import is_in_function_scope, is_in_class_scope
from obscurepy.utils.name import hex_name


def obscure_class_bases(node, tracker):
    """Obscures the Name nodes of a ClassDef node

    Args:
        **node (:obj: `ast.Name`)**: Current node to be obscured

        **tracker (:obj: `DefinitionTracker`)**: The instance of the definition tracker for checking if bases exist

    Returns:
        The obscured ast.Name node if it is the child of a ClassDef node, otherwise it is not obscured
    """
    if is_in_class_scope(node) and type(node.parent) != ast.Assign and node in node.parent.bases:
        if node.id in tracker.definitions['classes']:
            node.id = tracker.definitions['classes'][node.id]['new_name']

    return node


def handle_function_scope(node, tracker):
    """Internal method for handling names within the scope of a function

    Args:
        **node (:obj: `ast.Name`)**: Current Name node
    """
    if is_in_function_scope(node.parent):
        for function in tracker.definitions['functions'].values():
            if node.id in function['variables'] and node.id not in tracker.definitions['classes']:
                node.id = function['variables'][node.id]

    return node


def handle_global_scope(node, tracker):
    """Internal method for handling names within the global scope

    Args:
        **node (:obj: `ast.Name`)**: Current Name  node
    """
    if not is_in_function_scope(node.parent) and not is_in_class_scope(node.parent):
        if node.id != 'self':
            if node.id in tracker.definitions['variables']:
                node.id = tracker.definitions['variables'][node.id]['new_name']
            elif node.id not in [x['new_name'] for x in tracker.definitions['classes'].values()]:
                tracker.add_variable(
                    {'prev_name': node.id, 'new_name': hex_name(node.id)})
                node.id = tracker.definitions['variables'][node.id]['new_name']

    return node


def handle_class_scope(node, tracker):
    """Internal method for handling names within the scope of a class

    Args:
        **node (:obj: `ast.Name`)**: Current Name node
    """
    if is_in_class_scope(node.parent):
        for class_ in tracker.definitions['classes'].values():
            if node.id in class_['variables'] and node.id not in tracker.definitions['classes']:
                node.id = tracker.definitions['classes'][class_[
                    'prev_name']]['variables'][node.id]

    return node


class NameHandler(Handler):
    """Class to traverse and modify Name nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when NameHandler should be executed
    """

    def __init__(self, log=False, verbose=False):
        """Creates a new instance of a NameHandler"""
        super(NameHandler, self).__init__(log, verbose)
        self.execution_priority = 6

    def visit_Name(self, node):
        """Overrides the NodeTransformer visit_Name method. This method makes modifications
           to the abstract syntax tree  when it encounters a Name node

           Args:
               **node (:obj: `ast.Name`)**: The current Name node to be modified

            Returns:
                The modified Name node
        """
        self.logger.info('visit_Name')
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.id, str):
            node = obscure_class_bases(node, tracker)
            node = handle_global_scope(node, tracker)
            node = handle_class_scope(node, tracker)
            node = handle_function_scope(node, tracker)

        return node

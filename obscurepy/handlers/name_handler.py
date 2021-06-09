import ast
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.tree import is_in_function_scope, is_in_class_scope, is_in_call
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

        **tracker (:obj: `DefinitionTracker`)**: The instance of the definition tracker for checking scope

    Returns:
        An ast node
    """
    if is_in_function_scope(node.parent):
        if tracker.get_nested_in_function('variables', node.id):
            node.id = tracker.get_nested_in_function(
                'variables', node.id)['new_name']
        elif tracker.get_double_nested_in_function('variables', node.id):
            node.id = tracker.get_double_nested_in_function(
                'variables', node.id)['new_name']

    return node


def handle_global_scope(node, tracker):
    """Internal method for handling names within the global scope

    Args:
        **node (:obj: `ast.Name`)**: Current Name  node

        **tracker (:obj: `DefinitionTracker`)**: The instance of the definition tracker for checking scope

    Returns:
        An ast node
    """
    if not is_in_function_scope(node.parent) and not is_in_class_scope(node.parent):
        if node.id != 'self':
            if node.id in tracker.definitions['variables']:
                node.id = tracker.definitions['variables'][node.id]['new_name']
            elif node.id not in tracker.definitions['classes'] and node.id not in tracker.definitions['functions'] and type(node.parent) != ast.Call \
                    and type(node.parent) != ast.ClassDef:
                tracker.add_variable(
                    {'prev_name': node.id, 'new_name': hex_name(node.id)})
                node.id = tracker.definitions['variables'][node.id]['new_name']

    return node


def handle_class_scope(node, tracker):
    """Internal method for handling names within the scope of a class

    Args:
        **node (:obj: `ast.Name`)**: Current Name node

        **tracker (:obj: `DefinitionTracker`)**: The instance of the definition tracker for checking scope

    Returns:
        An ast node
    """
    if is_in_class_scope(node.parent):
        for class_ in tracker.definitions['classes'].values():
            if node.id in class_['variables'] and node.id not in tracker.definitions['classes']:
                node.id = tracker.definitions['classes'][class_[
                    'prev_name']]['variables'][node.id]['new_name']

    return node


def handle_calls(node, tracker):
    """Internal method for handling names inside ast.Call nodes

    Args:
        **node (:obj: `ast.Name`)**: Current Name node

        **tracker (:obj: `DefinitionTracker`)**: The instance of the definition tracker for checking scope

    Returns:
        An ast node
    """
    if is_in_call(node):
        if node.id in tracker.definitions['classes']:
            node.id = tracker.definitions['classes'][node.id]['new_name']
        elif node.id in tracker.definitions['functions']:
            node.id = tracker.definitions['functions'][node.id]['new_name']
        elif tracker.get_nested_in_function('functions', node.id):
            node.id = tracker.get_nested_in_function(
                'functions', node.id)['new_name']

    return node


def handle_returns(node, tracker):
    """Internal method for handling names inside ast.Return nodes

    Args:
        **node (:obj: `ast.Name`)**: Current Name node

        **tracker (:obj: `DefinitionTracker`)**: The instance of the definition tracker for checking scope

    Returns:
        An ast node
    """
    parent = None
    if type(node.parent) == ast.Return:
        # constant or variable
        parent = node.parent.parent
    elif type(node.parent.parent) == ast.Return:
        # call
        parent = node.parent.parent.parent
    if hasattr(parent, 'name'):
        if node.id in tracker.definitions['classes']:
            node.id = tracker.definitions['classes'][node.id]['new_name']
        elif node.id in tracker.definitions['functions']:
            node.id = tracker.definitions['functions'][node.id]['new_name']
        elif node.id in tracker.definitions['variables']:
            node.id = tracker.definitions['variables'][node.id]['new_name']
        elif tracker.get_nested_in_function('functions', node.id):
            node.id = tracker.get_nested_in_function(
                'functions', node.id)['new_name']
        elif tracker.get_nested_in_function('variables', node.id):
            node.id = tracker.get_nested_in_function(
                'variables', node.id)['new_name']

    return node


class NameHandler(Handler):
    """Class to traverse and modify Name nodes in an ast

    Attributes:
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
            node = handle_calls(node, tracker)
            node = handle_returns(node, tracker)
            self.generic_visit(node)

        return node

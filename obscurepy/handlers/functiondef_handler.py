import ast
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.utils.tree import is_in_class_scope, is_in_function_scope
from obscurepy.utils.name import hex_name


def get_variables(node):
    """Creates a dictionary of variables defined within a function body

    Args:
        **node (:obj: `ast.FunctionDef`)**: The node to get the variables of

    Returns:
        A dictionary with variable names for keys and obscured variable names as values
    """
    variables = {}
    for variable in node.body:
        if type(variable) == ast.Assign:
            for target in variable.targets:
                if type(target) == ast.Name:
                    variables[target.id] = hex_name(target.id)

    return variables


def get_args(node):
    """Creates a dictionary of parameters defined within a function body

    Args:
        **node (:obj: `ast.FunctionDef`)**: The node to get the args of

    Returns:
        A dictionary with arg names for keys and obscured arg names as values
    """
    args = {}
    for arg in node.args.args:
        args[arg.arg] = hex_name(arg.arg)

    return args


def get_functions(node):
    """Creates a dictionary of functions defined within a function body

    Args:
        **node (:obj: `ast.FunctionDef`)**: The node to get the functions of

    Returns:
        A dictionary with function names for keys and obscured function names as values
    """
    functions = {}
    for function in node.body:
        if type(function) == ast.FunctionDef:
            func_dict = create_function_dictionary(function)
            functions[function.name] = func_dict

    return functions


def get_return(node):
    """Creates a dictionary of returns defined within a function body

    Args:
        **node (:obj: `ast.FunctionDef`)**: The node to get the returns of

    Returns:
        A dictionary with return names for keys and obscured return names as values
    """
    return_ = {}
    for current_node in node.body:
        if type(current_node) == ast.Return:
            if type(current_node.value) == ast.Name:
                return_[current_node.value.id] = hex_name(
                    current_node.value.id)
            elif type(current_node.value) == ast.Call:
                return_[current_node.value.func.id] = hex_name(
                    current_node.value.func.id)

    return return_


def create_function_dictionary(node):
    """Creates a dictionary from a node describing a FunctionDef

    Args:
        **node (:obj: `ast.FunctionDef`)**: The node to create the dictionary for

    Returns:
        A dictionary
    """
    func_dict = {
        'new_name': hex_name(node.name),
        'prev_name': node.name,
        'variables': get_variables(node),
        'functions': get_functions(node),
        'args': get_args(node),
        'return': get_return(node),
    }

    return func_dict


def handle_global_scope(node, tracker):
    """Handles function definitions in the global scope

    Args:
        **node (:obj: `ast.FunctionDef`)**: The current node to handle

        **tracker (:obj: `DefinitionTracker`**: An instance of a DefinitionTracker

    Returns:
        The handled node
    """
    if not is_in_function_scope(node) and not is_in_class_scope(node):
        func_dict = create_function_dictionary(node)
        tracker.add_function(func_dict)
        node.name = tracker.definitions['functions'][node.name]['new_name']

    return node


def handle_class_scope(node, tracker):
    """Handles function definitions in a class scope

    Args:
        **node (:obj: `ast.FunctionDef`)**: The current node to handle

        **tracker (:obj: `DefinitionTracker`)**: An instance of a DefinitionTracker

    Returns:
        The handled node
    """
    if is_in_class_scope(node):
        for class_ in tracker.definitions['classes'].values():
            if node.name in class_['methods'] and class_['new_name'] == node.parent.name:
                func_dict = create_function_dictionary(node)
                func_dict['new_name'] = class_['methods'][node.name]
                class_['methods'][node.name] = func_dict
                node.name = class_['methods'][node.name]['new_name']

    return node


def handle_function_scope(node, tracker):
    """Handles function definitions in a function scope

    Args:
        **node (:obj: `ast.FunctionDef`)**: The current node to be handled

        **tracker (:obj: `DefinitionTracker`)**: An instance of a definition tracker

    Returns:
        The handled node
    """
    if is_in_function_scope(node):
        for function in tracker.definitions['functions'].values():
            if node.name in function['functions']:
                node.name = function['functions'][node.name]['new_name']
            elif node.parent.name == function['new_name']:
                func_dict = create_function_dictionary(node)
                function['functions'][func_dict['prev_name']] = func_dict
                node.name = function['functions'][node.name]['new_name']

    return node


class FunctionDefHandler(Handler):
    """Class to traverse and modify FunctionDef nodes in an ast

    Attributes:
        **execution_priority (int)**: Used to determine when FunctionHandler should be executed
    """

    def __init__(self, log=False, verbose=False):
        """Creates a new instance of a FunctionHandler"""
        super(FunctionDefHandler, self).__init__(log, verbose)
        self.execution_priority = 2

    def visit_FunctionDef(self, node):
        """Overrides the NodeTransformer visit_FunctionDef method. This method makes modifications
           to the abstract syntax tree and stores assignments with the DefinitionTracker class

        Args:
            **node (:obj: `ast.FunctionDef`)**: The current FunctionDef node to be modified

        Returns:
            The modified FunctionDef node
        """
        self.logger.info('visit_FunctionDef')
        tracker = DefinitionTracker.get_instance()
        if isinstance(node.name, str):
            node = handle_global_scope(node, tracker)
            node = handle_class_scope(node, tracker)
            node = handle_function_scope(node, tracker)
            self.generic_visit(node)

        return node

import ast
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.treeutils.function_scope_utils import *
from obscurepy.treeutils.class_scope_utils import *
from obscurepy.nameutils.name import hex_name


def get_variables(node):
    variables = {}
    for variable in node.body:
        if type(variable) == ast.Assign:
            for target in variable.targets:
                if type(target) == ast.Name:
                    variables[target.id] = hex_name(target.id)
    return variables


def get_args(node):
    args = {}
    for arg in node.args.args:
        args[arg.arg] = hex_name(arg.arg)
    return args


def get_return(node):
    return_ = {}
    for nd in node.body:
        if type(nd) == ast.Return:
            return_[nd.value.id] = hex_name(nd.value.id)
    return return_


def create_function_dictionary(node):
    func_dict = {
        'new_name': hex_name(node.name),
        'prev_name': node.name,
        'variables': get_variables(node),
        'args': get_args(node),
        'return': get_return(node),
    }
    return func_dict


def handle_global_scope(node, tracker):
    if not is_in_function_scope(node) and not is_in_class_scope(node):
        func_dict = create_function_dictionary(node)
        tracker.add_function(func_dict)
        node.name = tracker.definitions['functions'][node.name]['new_name']
    return node


def handle_class_scope(node, tracker):
    if is_in_class_scope(node):
        for class_ in tracker.definitions['classes'].values():
            if node.name in class_['methods'] and class_['prev_name'] == node.parent.name:
                func_dict = create_function_dictionary(node)
                func_dict['new_name'] = class_['methods'][node.name]
                class_['methods'][node.name] = func_dict
    return node


def handle_function_scope(node, tracker):
    if is_in_function_scope(node):
        pass
    return node


class FunctionDefHandler(Handler):
    """Class to traverse and modify FunctionDef nodes in an ast

    Attributes:
        **_debug_name (str)**: Name of class used for debugging purposes

        **execution_priority (int)**: Used to determine when FunctionHandler should be executed
    """

    def __init__(self):
        """Creates a new instance of a FunctionHandler"""
        super(FunctionDefHandler, self).__init__()
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
            node = handle_global_scope(node, tracker)
            node = handle_class_scope(node, tracker)
            node = handle_function_scope(node, tracker)

        return node

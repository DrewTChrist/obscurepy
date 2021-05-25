import ast
from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker
from obscurepy.treeutils.function_scope_utils import *
from obscurepy.treeutils.class_scope_utils import *


def get_variables(node):
    variables = []
    for variable in node.body:
        if type(variable) == ast.Assign:
            for target in variable.targets:
                if type(target) == ast.Name:
                    variables.append(target.id)
    return variables


def get_args(node):
    args = []
    for arg in node.args.args:
        args.append(arg.arg)
    return args


def get_return(node):
    return_ = None
    for nd in node.body:
        if type(nd) == ast.Return:
            return_ = nd.value.id
    return return_


def create_function_dictionary(node):
    func_dict = {
        'new_name': "",
        'prev_name': node.name,
        'variables': get_variables(node),
        'args': get_args(node),
        'return': get_return(node),
    }
    return func_dict


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
            func_dict = create_function_dictionary(node)
            tracker.add_function(func_dict)
            node.name = tracker.definitions['functions'][node.name]['new_name']
        return node

    def _handle_global_scope(self, node):
        if not is_in_function_scope(node) and not is_in_class_scope(node):
            # handle global function
            pass
        else:
            raise Exception('This FunctionDef is not in the global scope')

    def _handle_class_scope(self, node):
        if is_in_class_scope(node):
            # handle class function
            pass
        else:
            raise Exception('This FunctionDef is not in a class scope')

    def _handle_function_scope(self, node):
        if is_in_function_scope(node):
            # handle function within a function
            pass
        else:
            raise Exception('This FunctionDef is not in a function scope')

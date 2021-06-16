from obscurepy.handlers.handler import Handler
from obscurepy.utils.definition_tracker import DefinitionTracker


def handle_class_method_calls(node, tracker):
    if tracker.get_nested_in_class('methods', node.attr):
        node.attr = tracker.get_nested_in_class(
            'methods', node.attr)['new_name']

    return node


def handle_class_properties(node, tracker):
    if hasattr(node, 'value') and hasattr(node.value, 'id') and node.value.id == 'self':
        for class_ in tracker.definitions['classes'].values():
            if node.attr in class_['properties']:
                node.attr = class_['properties'][node.attr]
    return node


class AttributeHandler(Handler):
    """Class to traverse and modify Attribute nodes in an ast

    Attributes:
        **execution_priority (int)**: Used to determine when AttributeHandler should be executed
    """

    def __init__(self, log=False, verbose=False):
        """Creates a new instance of an AttributeHandler"""
        super(AttributeHandler, self).__init__(log, verbose)
        self.execution_priority = 4

    def visit_Attribute(self, node):
        """Overrides the NodeTransformer visit_Attribute method. This method makes modifications
           to the abstract syntax tree

        Args:
            **node (:obj: `ast.Attribute`)**: The current Attribute node to be modified

        Returns:
            The modified Attribute node
        """
        self.logger.info('visit_Attribute')
        tracker = DefinitionTracker.get_instance()
        node = handle_class_properties(node, tracker)
        node = handle_class_method_calls(node, tracker)
        return node

from dataclasses import dataclass, field
from obscurepy.models.obs_base import ObsBase
from obscurepy.models.obs_variable import ObsVariable


@dataclass
class ObsFunction(ObsBase):
    """Object to maintain data for python functions that have been visited

    Attributes:
        **return_value (str)**: Return value of of the represented function

        **arguments (set)**: A set of ObsVariables representing arguments

        **variables (set)**: A set of ObsVariables representing variables

        **functions (set)**: A set of ObsFunctions
    """
    return_value: str
    arguments: set[ObsVariable] = field(default_factory=set)
    variables: set[ObsVariable] = field(default_factory=set)
    functions: set['ObsFunction'] = field(default_factory=set)

    def add_variable(self, var: ObsVariable) -> None:
        """Adds an ObsVariable to the variables of an ObsFunction

        Args:
            **var (:obj: `ObsVariable`)**: The variable to add to the ObsFunction
        """
        if type(var) == ObsVariable:
            self.variables.add(var)
        else:
            raise TypeError('var must be an ObsVariable')

    def add_argument(self, var: ObsVariable) -> None:
        """Adds an ObsVariable to the arguments of an ObsFunction

        Args:
            **var (:obj: `ObsVariable`)**: The argument to add to the ObsFunction
        """
        if type(var) == ObsVariable:
            self.arguments.add(var)
        else:
            raise TypeError('var must be an ObsVariable')

    def add_function(self, var: 'ObsFunction') -> None:
        """Adds an ObsFunction to the functions of an ObsFunction

        Args:
            **var (:obj: `ObsFunction`)**: The function to add to the ObsFunction
        """
        if type(var) == ObsFunction:
            self.functions.add(var)
        else:
            raise TypeError('var must be an ObsFunction')

    def __hash__(self):
        """Hashes by new name and previous name"""
        return hash((self.new_name, self.prev_name))

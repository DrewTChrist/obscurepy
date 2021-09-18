from dataclasses import dataclass, field
from obscurepy.models.obs_base import ObsBase
from obscurepy.models.obs_variable import ObsVariable
from obscurepy.models.obs_function import ObsFunction


@dataclass
class ObsClass(ObsBase):
    """Object to maintain data for python classes that have been visited

    Attributes:
        **bases (tuple)**: A tuple of the bases a class inherits

        **properties (set)**: A set of ObsVariables holding class properties

        **methods (set)**: A set of ObsFunctions for class methods

        **classes (set)**: A set of ObsClasses for classes that may be inside another
    """
    bases: tuple[str]
    properties: set[ObsVariable] = field(default_factory=set)
    methods: set[ObsFunction] = field(default_factory=set)
    classes: set['ObsClass'] = field(default_factory=set)

    def add_property(self, var: ObsVariable) -> None:
        """Adds an ObsVariable to the properties of an ObsClass

        Args:
            **var (:obj: `ObsVariable`)**: The property to add to the ObsClass
        """
        if type(var) == ObsVariable:
            self.properties.add(var)
        else:
            raise TypeError('var must be an ObsVariable')

    def add_method(self, var: ObsFunction) -> None:
        """Adds an ObsFunction to the methods of an ObsClass

        Args:
            **var (:obj: `ObsFunction`)**: The function to add to the ObsClass
        """
        if type(var) == ObsFunction:
            self.methods.add(var)
        else:
            raise TypeError('var must be an ObsFunction')

    def add_class(self, var: 'ObsClass') -> None:
        """Adds an ObsClass to the methods of an ObsClass

        Args:
            **var (:obj: `ObsClass`)**: The class to add to the ObsClass
        """
        if type(var) == ObsClass:
            self.classes.add(var)
        else:
            raise TypeError('var must be an ObsClass')

    def __hash__(self):
        """Hashes by new name, previous name and base classes"""
        return hash((self.new_name, self.prev_name, self.bases))

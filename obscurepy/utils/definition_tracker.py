class DefinitionTracker:
    """Singleton class used to track definitions encountered while traversing the ast

    Attributes:
        **definitions (dict)**: A dictionary for storing definitions
    """

    _instance = None

    @classmethod
    def get_instance(cls):
        if DefinitionTracker._instance is None:
            cls()
        return DefinitionTracker._instance

    def __init__(self):
        if DefinitionTracker._instance is not None:
            raise Exception("This class is a singleton")
        else:
            DefinitionTracker._instance = self

        self.definitions = {'classes': {},
                            'functions': {},
                            'variables': {}}

    def add_class(self, class_):
        """Adds a class found in the ast to the definitions dictionary along with an obscure name

        Args:
            **class_ (dict)**: A dictionary describing the class
        """
        if class_:
            self.definitions['classes'][class_['prev_name']] = class_

    def get_class(self, class_):
        """Gets a class from the definitions dictionary

        Args:
            **class_ (str)**: Name of the class to get from the definitions

        Returns:
            A dictionary with the information of the class requested
        """
        if class_:
            return self.definitions['classes'][class_]

    def add_function(self, function):
        """Adds a function found in the ast to the definitions dictionary along with an obscure name

        Args:
            **function (dict)**: a dictionary describing the function to be added to the definitions
        """
        if function:
            self.definitions['functions'][function['prev_name']] = function

    def get_function(self, function):
        """Gets a function from the definitions dictionary

        Args:
            **function (str)**: the string name of the function to get

        Returns:
            A dictionary describing the function requested
        """
        if function:
            return self.definitions['functions'][function]

    def add_variable(self, variable):
        """Adds a variable found in the ast to the definitions dictionary along with an obscure name

        Args:
            **variable (dict)**: a dictionary describing the variable to be added to the definitions
        """
        if variable:
            self.definitions['variables'][variable['prev_name']] = variable

    def get_variable(self, variable):
        """Gets a variable from the definitions dictionary

        Args:
            **variable (str)**: the string name of the variable to get

        Returns:
            A dictionary describing the variable requested
        """
        if variable:
            return self.definitions['variables'][variable]

    def clear_definitions(self):
        self.definitions['classes'].clear()
        self.definitions['functions'].clear()
        self.definitions['variables'].clear()

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
            self.definitions['classes'][class_['prev_name']
                                        ]['new_name'] = self._name_class(class_['prev_name'])

    def get_class(self, class_):
        """Gets a class from the definitions dictionary

        Args:
            **class_ (str)**: Name of the class to get from the definitions

        Returns:
            A dictionary with the information of the class requested
        """
        if class_:
            return self.definitions['classes'][class_]

    def _name_class(self, class_):
        """Generates an obscure name based on the class name hex value added to the length of the classes definition
           dictionary

        Args:
            **class_ (str)**: name of the class to be obscured

        Returns:
            An obscured name for a class
        """
        return f"_{hex(len(self.definitions['classes']) + self._get_ascii_sum(class_))}"

    def _get_ascii_sum(self, string):
        """Returns the sum of the ascii values of a string

        Args:
            **string (str)**: string of which to get the ascii value

        Returns:
            The sum of the ascii values of the string provided
        """
        sum = 0
        for c in string:
            sum += int(ord(c))
        return sum

    def add_function(self, function):
        """Adds a function found in the ast to the definitions dictionary along with an obscure name

        Args:
            **function (dict)**: a dictionary describing the function to be added to the definitions
        """
        if function:
            self.definitions['functions'][function['prev_name']] = function
            self.definitions['functions'][function['prev_name']
                                          ]['new_name'] = self._name_function(function['prev_name'])

    def get_function(self, function):
        """Gets a function from the definitions dictionary

        Args:
            **function (str)**: the string name of the function to get

        Returns:
            A dictionary describing the function requested
        """
        if function:
            return self.definitions['functions'][function]

    def _name_function(self, function):
        """Generates an obscure name based on the function name hex value added to the length of the function definition
           dictionary

        Args:
            **function (str)**: name of the function to be obscured

        Returns:
            An obscured name for a function
        """
        return f"_{hex(len(self.definitions['functions']) + self._get_ascii_sum(function))}"

    def add_variable(self, variable):
        """Adds a variable found in the ast to the definitions dictionary along with an obscure name

        Args:
            **variable (dict)**: a dictionary describing the variable to be added to the definitions
        """
        if variable:
            self.definitions['variables'][variable] = self._name_variable(
                variable)

    def get_variable(self, variable):
        """Gets a variable from the definitions dictionary

        Args:
            **variable (str)**: the string name of the variable to get

        Returns:
            A dictionary describing the variable requested
        """
        if variable:
            # return [x for x in self.definitions['variables'] if x['name'] == variable][0]
            return self.definitions['variables'][variable]

    def _name_variable(self, variable):
        """Generates an obscure name based on the variable name hex value added to the length of the variable definition
           dictionary

        Args:
            **variable (str)**: name of the variable to be obscured

        Returns:
            An obscured name for a variable
        """
        return f"_{hex(len(self.definitions['variables']) + self._get_ascii_sum(variable))}"

    def clear_definitions(self):
        self.definitions['classes'].clear()
        self.definitions['functions'].clear()
        self.definitions['variables'].clear()

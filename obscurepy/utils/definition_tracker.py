class DefinitionTracker:
    """DefinitionTracker singleton"""

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

        self.definitions = {'classes': [],
                            'functions': [],
                            'variables': []}

    def add_class(self, class_):
        if class_:
            self.definitions['classes'].append(class_)

    def get_class(self, class_):
        if class_:
            return [x for x in self.definitions['classes'] if x['name'] == class_][0]

    def add_function(self, function):
        if function:
            self.definitions['functions'].append(function)

    def get_function(self, function):
        if function:
            return [x for x in self.definitions['functions'] if x['name'] == function][0]

    def add_variable(self, variable):
        if variable:
            self.definitions['variables'].append(variable)

    def get_variable(self, variable):
        if variable:
            return [x for x in self.definitions['variables'] if x['name'] == variable][0]

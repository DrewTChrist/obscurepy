class DefinitionTracker:

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

    def add_class(self, class_):
        pass

    def get_class(self, class_):
        pass

    def add_function(self, function):
        pass

    def get_function(self, function):
        pass

    def add_variable(self, variable):
        pass

    def get_variable(self, variable):
        pass

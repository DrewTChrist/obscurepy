from obscurepy.handlers.handler import Handler
from obscurepy.regex import class_re
import re


class ClassNameHandler(Handler):

    def __init__(self):
        super().__init__()
        self.replacement_name = "ClassFive"
        self.pattern = class_re

    def load_config(self):
        pass

    def can_process(self, text):
        if re.match(self.pattern, text):
            return True
        else:
            return False

    def process(self, text):
        match = re.match(self.pattern, text)
        text = re.sub(match.group(1), self.replacement_name, text)
        return text

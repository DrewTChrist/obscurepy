from obscurepy.handlers.class_name_handler import ClassNameHandler


class Obfuscator:

    def __init__(self, project=False):
        self.filenames = []
        self.chain = None
        self.text = []
        self.project = project
        self.tree = None

    def build_chain(self):
        self.chain = ClassNameHandler()

    def obfuscate(self):
        for i in range(0, len(self.text)):
            text = self.chain.handle(self.text[i])
            if text:
                self.text[i] = text

    def load_file(self, file):
        with open(file, 'r') as file:
            for line in file.readlines():
                self.text.append(line)
            file.close()

    def load_files(self, directory):
        pass



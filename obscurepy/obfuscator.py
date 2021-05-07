from obscurepy.utils.loader import load_handlers, load_config


class Obfuscator:
    """Obfuscator class"""

    def __init__(self):
        self.config = None
        self.filenames = []
        self.chain = None
        self.text = []
        self.tree = None

    def build_chain(self):
        self.chain = load_handlers()

    def load_config(self):
        self.config = load_config('config/config.yaml')

    def obfuscate(self):
        pass

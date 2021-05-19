from obscurepy.utils.loader import load_handlers, load_config


class Obfuscator:
    """Main obfuscator class for managing files, handlers and other processes

    Attributes:
        **config (dict)**: Configuration options

        **filenames (list)**: List of filenames to be obscured

        **chain (:obj: `Handler`)**: A single handler which is the first in the chain of handlers

        **text (str)**: Source code from a file

        **tree (:obj: `ast.Module`)**: Reference to the ast tree created from text attribute
    """

    def __init__(self):
        """Creates an instance of an Obfuscator"""
        self.config = None
        self.filenames = []
        self.chain = None
        self.text = []
        self.tree = None

    def build_chain(self):
        """Loads handlers and assigns the first one to chain"""
        self.chain = load_handlers()

    def load_config(self):
        """Loads configuration options"""
        self.config = load_config('config/config.yaml')

    def obfuscate(self):
        pass

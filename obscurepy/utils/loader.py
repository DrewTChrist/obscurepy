from obscurepy.handlers import *
import inspect
import sys
import yaml


def load_handlers():
    handlers = __create_handlers()

    for i in range(0, len(handlers) - 1):
        handlers[i].set_next(handlers[i + 1])

    return handlers[0]


def __create_handlers():
    handlers = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            handlers.append(obj())

    return handlers


def load_config(file):
    with open(file, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def load_file(file):
    text = []
    with open(file, 'r') as file:
        text = file.read()
        file.close()
    return text


def load_files(files):
    texts = []
    for file in files:
        texts.append(load_file(file))
    return texts

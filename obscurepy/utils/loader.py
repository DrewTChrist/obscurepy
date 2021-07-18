from obscurepy.handlers import *
import importlib
import inspect
import os
import sys
import yaml


def load_handlers(log, verbose):
    """Dynamically loads handler classes

    Returns:
        The first handler in the chain of handlers
    """
    handlers = create_handlers(log, verbose)

    return connect_handlers(handlers)


def load_custom_handlers(plugin_directory, log, verbose):
    try:
        handlers = create_handlers(log, verbose)
        plugin_names = [x.split('.')[0] for x in os.listdir(plugin_directory)
                        if x.split('.')[0] not in ['__pycache__', '__init__']]
        sys.path.append(os.getcwd())
        #plugins = importlib.import_module('plugins')
        plugins = importlib.import_module(plugin_directory.replace('/', '.'))
        for i in range(len(handlers)):
            if 'plugins' not in handlers[i].__module__:
                module_name = handlers[i].__module__.split('.')[2]
                class_name = type(handlers[i]).__name__
                if module_name in plugin_names:
                    module = getattr(plugins, module_name)
                    class_ = getattr(module, class_name)
                    replace_handler(handlers, class_(), log, verbose)
        return connect_handlers(handlers)
    except OSError:
        raise OSError('plugins directory does not exist')


def replace_handler(handlers, custom_handler, log, verbose):
    for i in range(len(handlers)):
        if type(handlers[i]).__name__ == type(custom_handler).__name__:
            handlers[i] = custom_handler

    return connect_handlers(handlers)


def connect_handlers(handlers):
    for i in range(0, len(handlers) - 1):
        handlers[i].set_next(handlers[i + 1])

    return handlers[0]


def create_handlers(log, verbose):
    """Dynamically creates handler classes

    Returns:
        A list of handlers sorted by execution priority
    """
    handlers = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            handlers.append(obj(log, verbose))

    handlers.sort(key=lambda x: x.execution_priority)

    return handlers


def load_config(file):
    """Loads yaml config files

    Args:
        **file (str)**: File path and name

    Returns:
        A dictionary of configuration options
    """
    if file:
        with open(file, 'r') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    else:
        raise ValueError('file cannot be None or empty')


def load_file(file):
    """Loads text from a file

    Args:
        **file (str)**: File path and name

    Returns:
        The text read from the requested file
    """
    text = ''
    if file:
        with open(file, 'r') as file:
            text = file.read()
            file.close()
        return text
    else:
        raise ValueError('file cannot be None or empty')


def load_files(files):
    """Loads text from multiple files

    Args:
        **files (list)**: List of paths to files to be read

    Returns:
        A list of the texts read in from each requested file
    """
    texts = []
    if files:
        for file in files:
            text = load_file(file)
            if text:
                texts.append(text)
        return texts
    else:
        raise ValueError('files cannot be None')

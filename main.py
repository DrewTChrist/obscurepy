import ast
from obscurepy.handlers.class_handler import ClassHandler
from obscurepy.handlers.function_handler import FunctionHandler


if __name__ == "__main__":
    with open('obscurepy/obfuscated.py', 'r') as file:
        text = file.read()
        file.close()

    tree = ast.parse(text)

    handler = ClassHandler()
    handler.set_next(FunctionHandler())

    tree = handler.handle(tree)

    print(ast.dump(tree, indent=4))
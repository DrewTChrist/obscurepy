class SomeRandomClass:

    def __init__(self):
        self.x = 50
        print('created some random class')

    def random_class_function(self, word):
        variable = 'somepath'
        print('some random stuff ' + word)


class AnotherClass:

    def __init__(self):
        self.y = 90
        print('do some stuff')

    def class_function_two(self):
        print('print more stuff')


class NumberTwo:

    def __init__(self):
        print('some stuff')

    def more_stuff(self):
        print('more stuff')

def not_a_class_function():
    print('hellohello')

def main():
    src = SomeRandomClass()

    src2 = NumberTwo()

    src.random_class_function('hello')



if __name__ == '__main__':
    main()
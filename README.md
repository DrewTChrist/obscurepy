# obscurepy

## Description

ARCHIVED

## Table of Contents

1. [Usage](#usage)
2. [License](#license)


### An example:
```python
class FirstClass:
    pass


class SecondClass(FirstClass):
    # this is a comment
    class_variable = 6

    def __init__(self, param_1):
        self.my_property = param_1

    def class_function(self, param_1, param_2):
        self.prop_1 = param_1
        self.prop_2 = param_2


def first_function():
    def with_another():
        c = 42
        return c
    return with_another()

def second_function(param_1, param_2, param_3):
    d = 'string'
    return d + str(param_1)

def third_function():
    e = 100.0
    return e

a = FirstClass()

b = SecondClass(1)

print(first_function())

print(second_function(1, 2, 3))

print(third_function())

a = SecondClass(1)

a.class_function(1, 2)

first_function()
```
```python
class _0x3fe:
    pass

class _0x452(_0x3fe):
    _0x5bb = int('0x6', 16)

    def __init__(_0x1aa, _0x2a1):
        _0x1aa._0x4ca = _0x2a1

    def _0x5db(_0x1aa, _0x2a1, _0x2a2):
        _0x1aa._0x251 = _0x2a1
        _0x1aa._0x252 = _0x2a2

def _0x5ed():

    def _0x50c():
        _0x63 = int('0x2a', 16)
        return _0x63
    return _0x50c()

def _0x641(_0x2a1, _0x2a2, _0x2a3):
    _0x64 = ''.join([chr(x) for x in [115, 116, 114, 105, 110, 103]])
    return _0x64 + str(_0x2a1)

def _0x5e0():
    _0x65 = float.fromhex('0x1.9000000000000p+6')
    return _0x65
_0x61 = _0x3fe()
_0x62 = _0x452(int('0x1', 16))
print(_0x5ed())
print(_0x641(int('0x1', 16), int('0x2', 16), int('0x3', 16)))
print(_0x5e0())
_0x61 = _0x452(int('0x1', 16))
_0x61._0x5db(int('0x1', 16), int('0x2', 16))
_0x5ed()
```

## Usage
The following command can be used to obscure a single file:
```shell
obscure --filepath=my_module.py
```

The following command can be used to obscure a multi file project:
```shell
obscure --project_dir=my_project
```

Alternatively, you can specify an output directory for both single file and multi file obscuring:
```shell
obscure --filepath=my_module.py --output_dir=desired_output_directory
```
```shell
obscure --project_dir=my_project --output_dir=desired_output_directory
```

## License
MIT License

Copyright (c) 2021 Andrew Christiansen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

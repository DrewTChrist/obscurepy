# obscurepy
[![Build Status](https://travis-ci.com/DrewTChrist/obscurepy.svg?branch=master)](https://travis-ci.com/DrewTChrist/obscurepy)
[![codecov](https://codecov.io/gh/DrewTChrist/obscurepy/branch/master/graph/badge.svg?token=2LN7K8W2PZ)](https://codecov.io/gh/DrewTChrist/obscurepy)

## Description
A tool for obscuring, or making python source code difficult to read.

## Table of Contents

1. [Installation](#installation)
2. [Limitations](#limitations)
3. [Usage](#usage)
4. [License](#license)

## Installation
This command will install obscurepy:
```shell
python -m pip install obscurepy
```
I would recommend installing it in a virtual environment as opposed to globally:
```shell
python -m venv venv
source venv/bin/activate
python -m pip install obscurepy
```

## Limitations
As this program is still in active development, there are many limitations. Below is a list of things obscurepy can and
can't do, along with an example.

### Things that obscurepy can currently do:
* Obscure class definitions
* Obscure class calls (without arguments)
* Obscure class properties
* Obscure function definitions (without parameters)
* Obscure function calls (without arguments)
* Obscure string constants
* Obscure integer constants
* Obscure float constants

### Things it cannot do:
* Anything else

### An example:
```python
class FirstClass:
    pass


class SecondClass(FirstClass):
    # this is a comment
    class_variable = 6

    def __init__(self):
        self.my_property = 8

    def class_function(self):
        self.new_property = 10


def first_function():
    c = 42


def second_function():
    d = 'string'

def third_function():
    e = 100.0

a = FirstClass()

b = SecondClass()

first_function()

```
```python
class _0x3fe:
    pass

class _0x452(_0x3fe):
    _0x5bb = int('0x6', 16)

    def __init__(self):
        self._0x4ca = int('0x8', 16)

    def _0x5db(self):
        self._0x52e = int('0xa', 16)

def _0x5ed():
    _0x63 = int('0x2a', 16)

def _0x641():
    _0x64 = ''.join([chr(x) for x in [115, 116, 114, 105, 110, 103]])

def _0x5e0():
    _0x65 = float.fromhex('0x1.9000000000000p+6')
_0x61 = _0x3fe()
_0x62 = _0x452()
_0x5ed()
_0x641()
_0x5e0()
_0x61 = _0x452()
```

## Usage
The following command can be used to obscure a single file:
```shell
obscure --filepath=my_module.py
```

The following command can be used to obscure a multi file project:
```shell
obscure -p --project_dir=my_project
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

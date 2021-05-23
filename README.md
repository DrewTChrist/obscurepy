# obscurepy
[![Build Status](https://travis-ci.com/DrewTChrist/obscurepy.svg?branch=master)](https://travis-ci.com/DrewTChrist/obscurepy)
[![codecov](https://codecov.io/gh/DrewTChrist/obscurepy/branch/master/graph/badge.svg?token=2LN7K8W2PZ)](https://codecov.io/gh/DrewTChrist/obscurepy)

## Description
A tool for obscuring, or making python source difficult to read.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Credits](#credits)
4. [License](#license)

## Installation
This command will install obscurepy:
```shell
python -m pip install git+https://github.com/drewtchrist/obscurepy.git
```
I would recommend installing it in a virtual environment as opposed to globally:
```shell
python -m venv venv
source venv/bin/activate
python -m pip install git+https://github.com/drewtchrist/obscurepy.git
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

Alternatively, you can specifiy an output directory for both single file and multi file obscuring:
```shell
obscure --filepath=my_module.py --output_dir=desired_output_directory
```
```shell
obscure --project_dir=my_project --output_dir=desired_output_directory
```

## Credits

## License

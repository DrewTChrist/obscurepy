# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

### Changed

### Removed

## [0.6.0](https://github.com/drewtchrist/obscurepy/releases/tag/v0.6.0) - 2021-05-24
### Added
* Added deployment scripts for pypi and testpypi
* Added a license
* Added a NameHandler class (unimplemented)
* Added a ConstantHandler class, it now obscures strings, integers and floats
* Added tests for obscure.py

### Changed
* Updated readme
* Updated travis.yml to deploy to pypi

### Removed

## [0.5.0](https://github.com/drewtchrist/obscurepy/releases/tag/v0.5.0) - 2021-05-23
### Added
* Added better functionality for ClassDefHandler building dictionaries of classes
* Added better funtionality for FunctionDefHandler building dictionaries of functions
* Added obscurepy/scripts/obscure.py which holds a click based command line interface

### Changed
* Updated class and sequence diagrams
* Updated setup.py to properly integrate with click
* Updated the readme with installation and usage instructions

### Removed

## [0.4.0](https://github.com/drewtchrist/obscurepy/releases/tag/v0.4.0) - 2021-05-21
### Added
* Added functionality to the Obfuscator class to complete the pipeline from file to tree to obfuscated file
* Added support for pre 3.9 versions of python, since ast.unparse released in 3.9, astunparse was the library used
* Added several tests for the Obfuscator class

### Changed

### Removed

## [0.3.1](https://github.com/drewtchrist/obscurepy/releases/tag/v0.3.1) - 2021-05-20
### Added

### Changed
* codecov is working

### Removed

## [0.3.0](https://github.com/drewtchrist/obscurepy/releases/tag/v0.3.0) - 2021-05-20
### Added
* Added treeutils package
* Added treeutils.class_scope_utils.py
* Added treeutils.function_scope_utils.py
* Added tests for treeutils package
* Added scripts/coverage.sh to execute code coverage reports
* Added coverage.sh to .travis.yml

### Changed
* utils.tree.py is now treeutils.general.py

### Removed

## [0.2.3](https://github.com/drewtchrist/obscurepy/releases/tag/v0.2.3) - 2021-05-19
### Added

### Changed
* Made front page links visible again

### Removed

## [0.2.2](https://github.com/drewtchrist/obscurepy/releases/tag/v0.2.2) - 2021-05-19
### Added

### Changed
* Made docs cleaner by grouping modules in the same package together

### Removed

## [0.2.1](https://github.com/drewtchrist/obscurepy/releases/tag/v0.2.1) - 2021-05-19
### Added

### Changed
* Changed sphinx documentation theme to "read the docs"

### Removed

## [0.2.0](https://github.com/drewtchrist/obscurepy/releases/tag/v0.2.0) - 2021-05-19
### Added
* Added assign_handler.py to handle ast.Assign nodes
* Added call_handler.py to handle ast.Call nodes
* Added a _debug_name property to handlers
* Added an execution_priority property to handlers to sort their execution order
* Added methods to DefinitionTracker to name classes, functions and variables that are added to definitions
* Added a new module in utils called tree.py, it contains a function to add a parent reference to all ast nodes
  this may be useful for determining the scope of variables
* Added tests for CallHandler, AssignHandler, ClassHandler, FunctionHandler and a test for the complete chain

### Changed
* Changed string_literal_handler.py and StringLiteralHandler to just literal_handler.py and LiteralHandler
* Updated docstrings for sphinx
* Changed DefinitionTracker.definitions to hold dictionaries instead of lists
* obscurepy.utils.loader.__create_handlers() now sorts them by execution_priority

### Removed
* Removed methods.md

## [0.1.3](https://github.com/drewtchrist/obscurepy/releases/tag/v0.1.3) - 2021-05-08
### Added

### Changed
* Added build status badge to readme
* Travis ci pipeline is now working for tests

### Removed

## [0.1.2](https://github.com/drewtchrist/obscurepy/releases/tag/v0.1.2) - 2021-05-07
### Added

### Changed
* Updated readme

### Removed

## [0.1.1](https://github.com/drewtchrist/obscurepy/releases/tag/v0.1.1) - 2021-05-07
### Added
* Added some test classes
* Added .travis.yml

### Changed

### Removed

## [0.1.0](https://github.com/drewtchrist/obscurepy/releases/tag/v0.1.0) - 2021-05-06
### Added
* Added some basic handlers
* Added some basic utils
* Added some basic diagrams
* Setup documents
* Setup pre commit hooks

### Changed

### Removed

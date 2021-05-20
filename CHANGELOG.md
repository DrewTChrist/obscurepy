# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

### Changed

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

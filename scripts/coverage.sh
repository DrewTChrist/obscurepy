#!/bin/sh

# run from root of project
# usage: scripts/coverage.sh

coverage run --source=./obscurepy -m unittest discover -s ./tests -t ./

coverage report

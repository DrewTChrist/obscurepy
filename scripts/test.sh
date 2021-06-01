#!/bin/sh

# run from root of project
# usage: scripts/test.sh

python -m unittest discover -s ./tests -t ./

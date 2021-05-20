#!/bin/sh

coverage run --source=./obscurepy -m unittest discover -s ./ -t ./

coverage report

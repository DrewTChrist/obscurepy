#!/bin/sh

cd tests

coverage run --source=../obscurepy -m unittest discover -s ./ -t ../

coverage report

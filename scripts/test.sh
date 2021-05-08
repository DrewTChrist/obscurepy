#!/bin/sh

cd tests

python -m unittest discover -s ./ -t ../

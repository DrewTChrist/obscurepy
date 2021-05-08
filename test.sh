#!/bin/sh

cd tests

python -m unittest discover -s $HOME/obscurepy/tests -t $HOME/obscurepy

#!/bin/sh

# run from root of project
# usage: scripts/release.sh 0.1.0,0.1.1,added,"added this",changed,"changed this",removed,"removed this"

# delimit by commas
IFS=','

# Build source rsts
sphinx-apidoc -f -o sphinx/source obscurepy

# run python release script
python scripts/release.py $@

cd sphinx

# build documentation
make github

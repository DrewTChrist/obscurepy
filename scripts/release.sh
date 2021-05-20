#!/bin/sh

python scripts/release.py "$1" "$2"

while getopts a:c:r: flag
do
    case "${flag}" in
        a) username=${OPTARG};;
        c) age=${OPTARG};;
        r) fullname=${OPTARG};;
        *);;
    esac
done

sphinx-apidoc -f -o sphinx/source obscurepy

cd sphinx

make github

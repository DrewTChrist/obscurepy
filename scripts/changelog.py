#!/usr/bin/python

import sys


def update_version_number(file_name):
    old_version = sys.argv[1]
    new_version = sys.argv[2]
    try:
        with open(file_name, 'r+') as file:
            text = file.readlines()
            for i in range(len(text)):
                if old_version in text[i]:
                    text[i] = text[i].replace(old_version, new_version)
            file.seek(0)
            file.writelines(text)
            file.truncate()
    except Exception as e:
        print(e)
    finally:
        file.close()


if __name__ == '__main__':
    update_version_number('setup.py')
    update_version_number('sphinx/source/conf.py')

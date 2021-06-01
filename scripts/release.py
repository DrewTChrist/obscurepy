#!/usr/bin/python

import sys
from changelog import add_to_changelog


def parse_args(args):
    added = False
    changed = False
    removed = False
    a_list = []
    c_list = []
    r_list = []
    for arg in args:
        if arg == 'added':
            added = True
            changed = False
            removed = False
            continue
        elif arg == 'changed':
            added = False
            changed = True
            removed = False
            continue
        elif arg == 'removed':
            added = False
            changed = False
            removed = True
            continue
        if added:
            a_list.append(arg)
        elif changed:
            c_list.append(arg)
        elif removed:
            r_list.append(arg)
    return a_list, c_list, r_list


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


def update_modules_rst():
    try:
        with open('sphinx/source/modules.rst', 'r+') as file:
            text = file.readlines()
            text[0] = 'Documentation\n'
            text[1] = '=============\n'
            file.seek(0)
            file.writelines(text)
            file.truncate()
    except Exception as e:
        print(e)
    finally:
        file.close()


if __name__ == '__main__':
    changelog_updates = parse_args(sys.argv[3:])
    update_version_number('setup.py')
    update_version_number('sphinx/source/conf.py')
    add_to_changelog(sys.argv[2], changelog_updates[0],
                     changelog_updates[1], changelog_updates[2])
    update_modules_rst()

#!/usr/bin/python

import datetime


def write_updates(update_list, file_text, header):
    new_text = file_text
    index = new_text.find(header) + len(header)
    for update in update_list:
        new_text = new_text[:index] + f"* {update}\n" + new_text[index:]
        index += len(f"* {update}\n")
    return new_text


def write_added(added_list, file_text):
    return write_updates(added_list, file_text, '### Added\n')


def write_changed(changed_list, file_text):
    return write_updates(changed_list, file_text, '### Changed\n')


def write_removed(removed_list, file_text):
    return write_updates(removed_list, file_text, '### Removed\n')


def insert_changelog_entry(entry, file_text):
    new_text = None
    unreleased_entry = "## [Unreleased]\n" \
                       "### Added\n\n" \
                       "### Changed\n\n" \
                       "### Removed\n\n"
    index = file_text.find(unreleased_entry) + len(unreleased_entry)
    new_text = file_text[:index] + entry + file_text[index:]
    return new_text


def add_to_changelog(new_version, added, changed, removed):
    file_text = None
    changelog_entry = f"## [{new_version}]" \
                      f"(https://github.com/drewtchrist/obscurepy/releases/tag/v{new_version}) - " \
                      f"{datetime.date.today()}\n" \
                      "### Added\n\n" \
                      "### Changed\n\n" \
                      "### Removed\n\n"

    with open('CHANGELOG.md', 'r+') as file:
        file_text = file.read()
        changelog_entry = write_added(added, changelog_entry)
        changelog_entry = write_changed(changed, changelog_entry)
        changelog_entry = write_removed(removed, changelog_entry)
        file_text = insert_changelog_entry(changelog_entry, file_text)
        file.seek(0)
        file.write(file_text)
        file.truncate()
        file.close()

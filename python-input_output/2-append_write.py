#!/usr/bin/python3
"""Module for appending text to files."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file."""
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)

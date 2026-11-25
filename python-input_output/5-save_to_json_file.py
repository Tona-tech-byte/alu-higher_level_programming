#!/usr/bin/python3
"""Module for saving Python objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file using JSON representation."""
    with open(filename, mode="w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)

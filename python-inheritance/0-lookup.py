#!/usr/bin/python3
"""Module containing a function to list object attributes."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)

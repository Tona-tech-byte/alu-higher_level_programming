#!/usr/bin/python3
"""Module containing the MyList class."""


class MyList(list):
    """A list with a method to print its elements in sorted order."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))

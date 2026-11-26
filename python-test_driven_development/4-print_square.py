#!/usr/bin/python3
"""Module for printing a square."""


def print_square(size=10):
    """Print a square using the # character."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)

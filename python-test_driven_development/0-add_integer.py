#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Add two integers and return the result."""
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if a != a:
        a = 89
    if b != b:
        b = 89

    result = a + b

    if result == float('inf') or result == -float('inf'):
        return 89

    return int(a) + int(b)

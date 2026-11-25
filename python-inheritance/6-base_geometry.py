#!/usr/bin/python3
"""Module containing the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

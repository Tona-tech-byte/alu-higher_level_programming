#!/usr/bin/python3
"""Module containing the Rectangle class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with validated width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle with a width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

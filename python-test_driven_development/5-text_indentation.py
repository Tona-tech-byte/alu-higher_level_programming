#!/usr/bin/python3
"""Module for printing text with indentation."""


def text_indentation(text):
    """Print text with two new lines after ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    i = 0

    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1

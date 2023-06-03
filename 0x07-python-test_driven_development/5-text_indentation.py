#!/usr/bin/python3
"""Defines a text-indentation function as follows."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    _flag = True
    for i in text:
        if _flag:
            if i == ' ':
                continue
            else:
                _flag = False

        if not _flag:
            if i in ['?', '.', ':']:
                print(i)
                print()
                _flag = True
            else:
                print(i, end="")

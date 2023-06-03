#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max int in a list of int
        If the list is empty, the function returns None Items
    """
    if len(list) == 0:
        return None
    outcome = list[0]
    i = 1
    while i < len(list):
        if list[i] > outcome:
            outcome = list[i]
        i += 1
    return outcome

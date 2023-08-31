#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    if list_of_integers:
        list_of_integers.sort()
        """This will pick from the last number"""
        return list_of_integers[-1]
    return None

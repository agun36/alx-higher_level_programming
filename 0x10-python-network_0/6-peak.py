#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """fid the list of number and look from the last """
    if not list_of_integers:
        return None
    mid = len(list_of_integers)
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    if list_of_integers[mid] > list_of_integers[mid - 1] and
        list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid + 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[mid + 1:])
    return find_peak(list_of_integers[:mid])

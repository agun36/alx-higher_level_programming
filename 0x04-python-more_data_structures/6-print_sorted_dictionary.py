#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for key, value in sorted(a_dictionary.items()):
        print(key + ':', value)


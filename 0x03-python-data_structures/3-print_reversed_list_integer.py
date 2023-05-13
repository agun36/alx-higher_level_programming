#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list, in reverse order. 
    One integer per line.
    """
    for i in reversed(my_list):
        print("{}".format(i))

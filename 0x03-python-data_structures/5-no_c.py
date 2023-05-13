#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if ord(char) != ord("c") and ord(char) != ord("C"):
            new_string += char
            return new_string

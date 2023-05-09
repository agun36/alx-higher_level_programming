#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_val = ord(c)
        if ascii_val >= 97 and ascii_val <= 122:
            ascii_val -= 32
        print("{}".format(chr(ascii_val)), end="")
    print("")


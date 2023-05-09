#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord(c) <= 97 and ord(c) <= 122:
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()


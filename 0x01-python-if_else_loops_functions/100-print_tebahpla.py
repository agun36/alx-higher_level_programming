#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 == 0:
        letter = chr(i+32)
    else:
        letter = chr(i)
    print("{}".format(letter), end="")

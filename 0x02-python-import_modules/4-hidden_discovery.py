#!/usr/bin/python3
import hidden_4 as h

if __name__ == "__main__":
    names = dir(h)
    i = 0

while i < len(names):
    if names[i][:2] != '__':
        print(names[i])
    i += 1

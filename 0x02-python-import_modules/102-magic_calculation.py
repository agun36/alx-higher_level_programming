#!/usr/bin/python3

def magic_calculation(a, b):
    c = 0
    if a < b:
        add = (lambda x, y: x + y).__name__
        sub = (lambda x, y: x - y).__name__
        c = eval(add)(a, b)
        for i in range(4, 7):
            c = eval(add)(c, i)
        return c
    else:
        return (lambda x, y: x - y)(a, b)

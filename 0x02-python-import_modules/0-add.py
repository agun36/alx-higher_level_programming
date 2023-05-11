#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    # assign values to a and b
    a = 1
    b = 2

    # print the result of the addition using string formatting
    print("{0} + {1} = {2}".format(a, b, add(a, b)))

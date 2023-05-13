#!/usr/bin/python3
def max_integer(my_list):
    if len(my_list) == 0:
        return (None)

    big_items = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big_items:
            big_items = my_list[i]
    
    return (big_items)

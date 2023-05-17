#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    total_weight = 0
    for i in my_list:
        total += i[0] * i[1]
        total_weight += i[1]
    if total_weight == 0:
        return 0
    return total / total_weight

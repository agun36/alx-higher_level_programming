#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    empty_count = []
    for j in range(list_length):
        try:
            re = my_list_1[j]/my_list_2[j]
        except IndexError:
            print("out of range")
            re = 0
        except TypeError:
            print("wrong type")
            re = 0
        except ZeroDivisionError:
            print("division by 0")
            re = 0       
        finally:
            empty_count.append(re)
    return empty_count

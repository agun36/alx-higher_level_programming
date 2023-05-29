#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []    
    for j in range(list_length):
        try:
            result = my_list_1[j]/my_list_2[j]
        except (TypeError, ValueError):
            print("wrong type")
            result = 0    
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0 
        finally:
            new.append(result)
    return new

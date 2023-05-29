#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    output = ''
    try:
        for i in my_list:
            if count >= x:
                break
            output += str(i)
            count += 1
    except Exception as e:
        print ("Error", str(e))
    print(output)
    return (count)

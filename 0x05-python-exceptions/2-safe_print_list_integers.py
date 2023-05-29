#!/urs/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
             print("{:d}".format(my_list[i]), end="")
             count += 1
        except (TypeError, ValueError):
            print("An error occurred: Invalid type for my_list or x")
    print()
    return (count)

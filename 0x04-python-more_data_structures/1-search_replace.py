#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate over each element in the original list
    for key in my_list:
        # Check if the element matches the search element
        if key == search:
            # If it matches, replace it with the new element
            new_list.append(replace)
        else:
            # If it doesn't match, keep the element as it is
            new_list.append(key)

    return new_list

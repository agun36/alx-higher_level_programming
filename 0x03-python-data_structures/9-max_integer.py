#!/usr/bin/python3
def max_integer(my_list=[]):
  if not my_list:
    return None
  else:
    max_int = my_list[0]
    for item in my_list:
      if item > max_int:
        max_int = item
    return max_int

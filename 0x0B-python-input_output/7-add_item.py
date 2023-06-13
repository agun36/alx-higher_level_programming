#!/usr/bin/python3
"""create a function that adds all arguments to a Python list"""

import sys
import json
import os.path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

my_items = []

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    my_items = load_from_json_file(filename)

if len(sys.argv) > 1:
    for elem in sys.argv[1:]:
        my_items.append(elem)

save_to_json_file(my_items, filename)

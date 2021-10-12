#!/usr/bin/python3
"""Load, add, save module"""


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file
from sys import argv

filename = "add_item.json"

try:
    my_list = load(filename)
except:
    my_list = []
for i in range(1, len(argv)):
        my_list.append(argv[a])
save(my_list, filename)

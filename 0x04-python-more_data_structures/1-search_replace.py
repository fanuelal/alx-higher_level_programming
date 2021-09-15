#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = my_list.index(search)
    new_list = my_list.copy()
    new_list[i] = replace
    return new_list

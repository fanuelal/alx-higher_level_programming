#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i++
        except:
            pass
    print()
    return i

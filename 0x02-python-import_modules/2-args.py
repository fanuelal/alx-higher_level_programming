#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    count = num - 1
    if num == 1:
        print("{} arguments.".format(count))
    elif num == 2:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))
    for i in range(1, num):
        print("{}: {}".format(i, sys.argv[i]))

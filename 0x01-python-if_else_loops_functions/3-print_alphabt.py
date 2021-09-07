#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c == ord('q') or c == ord('e'):
        continue
    print("{:c}".format(c), end="")

#!/usr/bin/env python3
import sys

# แสดงแค่ 8 ตัว
def shrink(string):
    print(string[:8])

#  เติม Z จน 8 ตัว
def enlarge(string):
    print(string + 'Z' * (8 - len(string)))


if len(sys.argv) == 1:
    print("none")
else:
    # loop 
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:  # length == 8
            print(param)
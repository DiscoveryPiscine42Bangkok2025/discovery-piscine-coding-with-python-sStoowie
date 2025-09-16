#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    string = sys.argv[1]
    z_count = string.lower().count('z')

    if z_count > 0:
        print('z' * z_count)
    else:
        print("none")
else:
    print("none")
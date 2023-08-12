#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    args = sys.argv[1:]

    for values in args:
        total = total + int(values)
    print(total)

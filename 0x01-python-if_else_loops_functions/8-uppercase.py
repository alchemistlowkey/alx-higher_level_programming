#!/usr/bin/python3
def uppercase(str):
    alpha = ""
    for c in str:
        if 'a' <= c <= 'z':
            alpha += chr(ord(c) - 32)
        else:
            alpha += c
    print("{:s}".format(alpha))

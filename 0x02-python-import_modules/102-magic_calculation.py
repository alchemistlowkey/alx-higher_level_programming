#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_10 import add, sub

    if a < b:
        c = add(a, b)
        for values in range(4, 6):
            c = add(c, values)
        return c
    else:
        return sub(a, b)

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for keys, values in new.items():
        new[keys] = values * 2
    return new

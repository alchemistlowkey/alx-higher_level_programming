#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for keys, values in a_dictionary.items():
        if value == values:
            new.append(keys)
    for keys in new:
        del a_dictionary[keys]
    return a_dictionary

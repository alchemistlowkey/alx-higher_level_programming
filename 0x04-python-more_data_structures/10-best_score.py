#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max_v = 0
        max_k = None
        for keys, values in a_dictionary.items():
            if values > max_v:
                max_k = keys
                max_v = values
        return max_k

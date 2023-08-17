#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        total = 0
        initial = 0
        for values in roman_string:
            count = roman_dict.get(values, 0)
            if count > initial:
                total += count - 2 * initial
            else:
                total += count
            initial = count
        return total

#!/usr/bin/python3
def remove_char_at(str, n):
    if (n < 0) or (n >= len(str)):
        return str
    str1 = ""
    for i in range(len(str)):
        if i != n:
            str1 += str[i]
    return str1

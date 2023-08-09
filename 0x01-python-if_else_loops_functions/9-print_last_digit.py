#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    last_digit = number[-1]
    last_digit = int(last_digit)
    print("{:d}".format(last_digit), end='')
    return last_digit

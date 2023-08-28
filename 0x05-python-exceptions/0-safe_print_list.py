#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    value = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            value += 1
    except:
        pass
    finally:
        print()
        return value

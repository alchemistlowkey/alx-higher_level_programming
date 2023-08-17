#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    else:
        product = 0
        sum_of = 0
        for x, y in my_list:
            product += (x * y)
            sum_of += y
            avg = product / sum_of
        return avg

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
last_number = str(number[-1])
last_number = int(last_number)
if int(number) >= 0:
    if last_number > 5:
        print("Last digit of {} is {} and is greater than 5"
                .format(number, last_number))
    elif last_number == 0:
        print("Last digit of {} is {} and is 0"
                .format(number, last_number))
    elif (last_number < 6) and (last_number != 0):
        print("Last digit of {} is {} and is less than 6 and not 0"
                .format(number, last_number))
else:
    if last_number == 0:
        print("Last digit of {} is {} and is 0"
                .format(number, last_number))
    else:
        print("Last digit of {} is -{} and is less than 6 and not 0"
                .format(number, last_number))

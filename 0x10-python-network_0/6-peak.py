#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers

    Arguments:
        list_of_integers - integers to search for

    Returns:
        The peak integer(s)
    """

    if not list_of_integers:
        return None

    back, front = 0, len(list_of_integers) - 1

    while back < front:
        center = (back + front) // 2
        if list_of_integers[center] > list_of_integers[center + 1]:
            front = center
        else:
            back = center + 1

    return list_of_integers[back]

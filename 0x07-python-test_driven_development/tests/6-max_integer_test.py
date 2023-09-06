#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    class for testing max_integer
    """

    def test_max_integer(self):
        """
        Test for list of positive integers
        """
        tester = [1, 2, 3, 8, 4]
        self.assertEqual(max_integer(tester), max(tester))

    def test_max_integer_neg(self):
        """
        Test for list of negative integers
        """
        tester = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(max_integer(tester), max(tester))

    def test_max_integer_mixed(self):
        """
        Test for list of positive and negative integers
        """
        tester = [1, 2, 3, 0, -4, -5, -6]
        self.assertEqual(max_integer(tester), max(tester))

    def test_max_integer_float(self):
        """
        Test for list of positive and negative float
        """
        tester = [0.1, 1.23, 2.345, 3.4567, -4.321, -3.21, -2.1, 0]
        self.assertEqual(max_integer(tester), max(tester))

    def test_max_integer_empty(self):
        """
        Test if an empty list is passed
        """
        tester = []
        self.assertEqual(max_integer(tester), None)

    def test_max_integer_dup(self):
        """
        Test for list of duplicate integers
        """
        tester = [1, 2, 3, 0, -4, -5, -6, 2, -4]
        self.assertEqual(max_integer(tester), max(tester))

    def test_max_integer_one(self):
        """
        Test if list just have one element
        """
        tester = [9]
        self.assertEqual(max_integer(tester), max(tester))

    def test_max_integer_first(self):
        """
        Test if the first element is the maximum
        """
        tester = [9, 2, 5, 8]
        self.assertEqual(max_integer(tester), max(tester))

    def test_max_integer_last(self):
        """
        Test if the last element is the maximum
        """
        tester = [2, 6, -9, 7, 3, 8]
        self.assertEqual(max_integer(tester), max(tester))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Tests for the base class
"""
import unittest
import os
import sys
import io
import pep8
import inspect
from contextlib import redirect_stdout
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    class for testing the Base class methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """
        Test that base.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        check = pep8style.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0, "Found code style errors.")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

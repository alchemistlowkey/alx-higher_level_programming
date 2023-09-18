#!/usr/bin/python3
"""
Tests for the base class
"""
import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    class for testing the Base class methods
    """
    
    def test_id_increment(self):
        '''
        Test that the id increments correctly for multiple
        instances of Base.
        '''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        '''
        Test that a custom id is correctly assigned to the instance.
        '''
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_increment_after_custom_id(self):
        '''
        Test that the id increments correctly after a custom id.
        '''
        b1 = Base()
        self.assertEqual(b1.id, 4)

    def test_to_json_string_empty(self):
        """Test to_json_string method with an empty list of dictionaries."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string method with None as the input."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_single_dict(self):
        """Test to_json_string method with a single dictionary."""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_to_json_string_multiple_dicts(self):
        """Test to_json_string method with multiple dictionaries."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 3, 1)
        dict1 = r1.to_dictionary()
        dict2 = r2.to_dictionary()
        json_string = Base.to_json_string([dict1, dict2])
        self.assertEqual(json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 1, "width": 5, "id": 2, "height": 3, "y": 0}]')

    def test_to_json_string_empty_dict(self):
        """Test to_json_string method with an empty dictionary."""
        json_string = Base.to_json_string([{}])
        self.assertEqual(json_string, '[{}]')

    def setUp(self):
        """Set up method to run before each test."""
        # Remove any existing Rectangle.json file before each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        """Tear down method to run after each test."""
        # Remove the created Rectangle.json file after each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test save_to_file method with None as input."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file method with an empty list."""
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_single_instance(self):
        """Test save_to_file method with a single instance."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"width": 10', content)
            self.assertIn('"height": 7', content)
            self.assertIn('"x": 2', content)
            self.assertIn('"y": 8', content)

    def test_save_to_file_multiple_instances(self):
        """Test save_to_file method with multiple instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"width": 10', content)
            self.assertIn('"height": 7', content)
            self.assertIn('"x": 2', content)
            self.assertIn('"y": 8', content)
            self.assertIn('"id": 2', content)
            self.assertIn('"width": 2', content)
            self.assertIn('"height": 4', content)
            self.assertIn('"x": 0', content)
            self.assertIn('"y": 0', content)

    def test_from_json_string_none(self):
        """Test from_json_string method with None as input."""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_empty(self):
        """Test from_json_string method with an empty string as input."""
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        """Test from_json_string method with valid JSON string."""
        json_str = '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'
        expected_result = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        result = Base.from_json_string(json_str)
        self.assertEqual(result, expected_result)

    def test_create_rectangle(self):
        """Test create method with a Rectangle instance."""
        rectangle_dict = {'id': 1, 'width': 3, 'height': 5, 'x': 1, 'y': 0}
        r1 = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 0)

    def test_create_square(self):
        """Test create method with a Square instance."""
        square_dict = {'id': 2, 'size': 3, 'x': 1, 'y': 0}
        s1 = Square.create(**square_dict)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 0)

    def test_load_from_file_rectangle(self):
        """Test load_from_file method with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_input:
            self.assertIn(rect, list_rectangles_output)

    def test_load_from_file_square(self):
        """Test load_from_file method with Square instances."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        for square in list_squares_input:
            self.assertIn(square, list_squares_output)

    @classmethod
    def setUpClass(cls):
        """Set up test class."""
        # Remove any existing CSV files from previous test runs
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method of Base class."""
        # Test with Rectangle instances
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        with open("Rectangle.csv", "r") as file:
            csv_lines = file.readlines()
            csv_lines = [line.strip() for line in csv_lines]

        # Check the content of the CSV file
        expected_csv = ["1,10,7,2,8", "2,2,4,0,0"]
        self.assertEqual(csv_lines, expected_csv)

        # Test with Square instances
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        with open("Square.csv", "r") as file:
            csv_lines = file.readlines()
            csv_lines = [line.strip() for line in csv_lines]

        # Check the content of the CSV file
        expected_csv = ["5,5,0,0", "6,7,9,1"]
        self.assertEqual(csv_lines, expected_csv)

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method of Base class."""
        # Test with Rectangle instances
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()

        for rect in list_rectangles_input:
            self.assertIn(rect, list_rectangles_output)

        # Test with Square instances
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        list_squares_output = Square.load_from_file_csv()

        for square in list_squares_input:
            self.assertIn(square, list_squares_output)


if __name__ == "__main__":
    unittest.main()

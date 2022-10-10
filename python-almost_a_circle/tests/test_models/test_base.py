#!/usr/bin/python3
""" base test """

import os
import json
from models.square import Square
from io import StringIO
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """Test for base class"""

    def test_isinstance(self):
        """test id for is isntance"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        b2 = Base(65)
        self.assertIsInstance(b2, Base)

    def test_positive(self):
        """test id for number positive"""
        case = Base(25)
        case_01 = Base()
        case_02 = Base()
        case_03 = Base()
        self.assertEqual(case.id, 25)
        case_01.id = 2
        self.assertEqual(case_01.id, 2)
        case_02.id = 3
        self.assertEqual(case_02.id, 3)
        case_03.id = 4
        self.assertEqual(case_03.id, 4)

    def test_negative(self):
        """test id for negative values"""
        negative_01 = Base(-12)
        negative_02 = Base(-25)
        self.assertEqual(negative_01.id, -12)
        self.assertEqual(negative_02.id, -25)

    def test_string(self):
        """test  id for string case"""
        string_01 = Base("unicornio")
        string_02 = Base("sagitario")
        self.assertEqual(string_01.id, "unicornio")
        self.assertEqual(string_02.id, "sagitario")

    def test_to_json_string_AND_from_json_string(self):
        """from json string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.r1 = Rectangle(3, 5, 1, id=9)
        cls.r3 = Rectangle(2, 4, id=11)
        cls.s1 = Square(5, id=99)
        cls.s2 = Square(7, 9, 1, id=78)

    def test_save_to_file_AND_load_from_file(self):
        list_rectangles_input = [self.r1, self.r3]

        Rectangle.save_to_file(list_rectangles_input)
        self.assertTrue(os.path.isfile('Rectangle.json'))
        with open('Rectangle.json', 'r') as f:
            r_total = sum(1 for _ in f)
        self.assertGreater(r_total, 0)
        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

        list_squares_input = [self.s1, self.s2]

        Square.save_to_file(list_squares_input)
        self.assertTrue(os.path.isfile('Square.json'))

        with open('Square.json', 'r') as f:
            s_total = sum(1 for _ in f)
        self.assertGreater(s_total, 0)
        list_squares_output = Square.load_from_file()

        for square in list_squares_input:
            self.assertIsInstance(square, Square)

        for square in list_squares_output:
            self.assertIsInstance(square, Square)

        Base._Base__nb_objects -= 4

    def test_create(self):
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(self.r1.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertEqual(r2.__str__(), '[Rectangle] (9) 1/0 - 3/5')
        self.assertFalse(self.r1 is r2)
        self.assertFalse(self.r1 == r2)

    def test_None(self):
        """
        Test to check from none empty
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

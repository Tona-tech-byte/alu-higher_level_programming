#!/usr/bin/python3
"""Unit tests for the Square class."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square."""

    def test_square_one_argument(self):
        square = Square(1)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)

    def test_square_two_arguments(self):
        square = Square(1, 2)
        self.assertEqual(square.x, 2)

    def test_square_three_arguments(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.y, 3)

    def test_square_four_arguments(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.id, 4)

    def test_size_must_be_integer(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_must_be_integer(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_must_be_integer(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_string_representation(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        square = Square(1, 2, 3, 4)
        expected = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected)


    def test_update_positional(self):
        square = Square(1)
        square.update(89)
        self.assertEqual(square.id, 89)
        square.update(89, 2)
        self.assertEqual(square.size, 2)
        square.update(89, 2, 3)
        self.assertEqual(square.x, 3)
        square.update(89, 2, 3, 4)
        self.assertEqual(square.y, 4)

    def test_update_keyword(self):
        square = Square(1)
        square.update(id=89, size=2, x=3, y=4)
        self.assertEqual(square.to_dictionary(), {
            'id': 89, 'size': 2, 'x': 3, 'y': 4
        })

    def test_create(self):
        square = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(square.to_dictionary(), {
            'id': 89, 'size': 1, 'x': 2, 'y': 3
        })

    def test_create_partial_arguments(self):
        self.assertEqual(Square.create(id=89).id, 89)
        self.assertEqual(Square.create(id=89, size=1).size, 1)
        self.assertEqual(
            Square.create(id=89, size=1, x=2).x, 2
        )

    def test_save_to_file_none(self):
        Square.save_to_file(None)

    def test_save_to_file_empty(self):
        Square.save_to_file([])

    def test_save_to_file_square(self):
        import os
        square = Square(1)
        Square.save_to_file([square])
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

    def test_load_from_file_missing(self):
        import os
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_existing(self):
        import os
        square = Square(1)
        Square.save_to_file([square])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Square)
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()

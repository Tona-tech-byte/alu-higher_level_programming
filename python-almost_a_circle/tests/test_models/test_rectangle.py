#!/usr/bin/python3
"""Unit tests for the Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle."""

    def test_rectangle_two_arguments(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_three_arguments(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.x, 3)

    def test_rectangle_four_arguments(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.y, 4)

    def test_rectangle_five_arguments(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 5)

    def test_width_must_be_integer(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_height_must_be_integer(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_x_must_be_integer(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_y_must_be_integer(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_string_representation(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")

    def test_to_dictionary(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        expected = {
            'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        }
        self.assertEqual(rect.to_dictionary(), expected)


    def test_display(self):
        from io import StringIO
        from contextlib import redirect_stdout

        rect = Rectangle(2, 2)
        output = StringIO()
        with redirect_stdout(output):
            rect.display()
        self.assertEqual(output.getvalue(), "##\n##\n")

        rect = Rectangle(2, 2, 1, 1)
        output = StringIO()
        with redirect_stdout(output):
            rect.display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_update_positional(self):
        rect = Rectangle(1, 1)
        rect.update(89)
        self.assertEqual(rect.id, 89)
        rect.update(89, 2)
        self.assertEqual(rect.width, 2)
        rect.update(89, 2, 3)
        self.assertEqual(rect.height, 3)
        rect.update(89, 2, 3, 4)
        self.assertEqual(rect.x, 4)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(rect.y, 5)

    def test_update_keyword(self):
        rect = Rectangle(1, 1)
        rect.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(rect.to_dictionary(), {
            'id': 89, 'width': 2, 'height': 3, 'x': 4, 'y': 5
        })

    def test_create(self):
        rect = Rectangle.create(
            id=89, width=1, height=2, x=3, y=4
        )
        self.assertEqual(rect.to_dictionary(), {
            'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })

    def test_create_partial_arguments(self):
        self.assertEqual(Rectangle.create(id=89).id, 89)
        self.assertEqual(Rectangle.create(id=89, width=1).width, 1)
        self.assertEqual(
            Rectangle.create(id=89, width=1, height=2).height, 2
        )
        self.assertEqual(
            Rectangle.create(
                id=89, width=1, height=2, x=3
            ).x, 3
        )

    def test_save_to_file_none(self):
        import os
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        import os
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_rectangle(self):
        import os
        rect = Rectangle(1, 2)
        Rectangle.save_to_file([rect])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_load_from_file_missing(self):
        import os
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_existing(self):
        import os
        rect = Rectangle(1, 2)
        Rectangle.save_to_file([rect])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Rectangle)
        os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()

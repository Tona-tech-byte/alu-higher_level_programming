#!/usr/bin/python3
"""Unittests for max_integer."""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_increasing_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_decreasing_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -10, -1]), -1)

    def test_duplicate_maximum(self):
        self.assertEqual(max_integer([3, 7, 7, 2]), 7)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 3.7, 2.4]), 3.7)


if __name__ == "__main__":
    unittest.main()

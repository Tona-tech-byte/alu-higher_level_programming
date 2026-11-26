#!/usr/bin/python3
"""Unit tests for the Base class."""

import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatic ID assignment."""
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_auto_id_increment(self):
        """Test that automatic IDs increase."""
        Base()
        obj = Base()
        self.assertEqual(obj.id, 2)

    def test_assigned_id(self):
        """Test assigning an ID directly."""
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_none(self):
        """Test JSON conversion with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test JSON conversion with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dictionary(self):
        """Test JSON conversion with a dictionary."""
        data = [{'id': 12}]
        result = Base.to_json_string(data)
        self.assertEqual(json.loads(result), data)

    def test_to_json_string_returns_string(self):
        """Test that JSON conversion returns a string."""
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        """Test JSON conversion from None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test JSON conversion from an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_data(self):
        """Test JSON conversion from a JSON string."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(result, [{'id': 89}])

    def test_from_json_string_returns_list(self):
        """Test that JSON conversion returns a list."""
        result = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()

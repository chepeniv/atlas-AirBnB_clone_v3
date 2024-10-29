#!/usr/bin/python3

import unittest
from models.city import City

class TestCityFile(unittest.TestCase):

    def test_city__init__(self):
        new_city = City()
        self.assertEqual(new_city.name, "")
        self.assertEqual(new_city.state_id, "")

    def test_property_name(self):
        pass

    def test_property_state_id(self):
        pass

    def test_property_places(self):
        pass

class TestCityDB(unittest.TestCase):

    def test_city__init__success(self):
        new_city = City()
        self.assertEqual(new_city.name, "")
        self.assertEqual(new_city.state_id, "")

    def test_city__init__failure(self):

    def test_property_name(self):
        pass

    def test_property_state_id(self):
        pass

    def test_property_places(self):
        pass

if __name__ == "__main__":
    unittest.main()

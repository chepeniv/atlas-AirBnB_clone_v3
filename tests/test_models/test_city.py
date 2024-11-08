#!/usr/bin/python3

import unittest
from models.city import City
from models import storage_type


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
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
        name = "John"
        state_id = "5-5-5-5"
        new_city = City(name=name, state_id=state_id)
        self.assertEqual(new_city.name, name)
        self.assertEqual(new_city.state_id, state_id)

    def test_city__init__failure(self):
        pass

    def test_property_name(self):
        pass

    def test_property_state_id(self):
        pass

    def test_property_places(self):
        pass

if __name__ == "__main__":
    unittest.main()

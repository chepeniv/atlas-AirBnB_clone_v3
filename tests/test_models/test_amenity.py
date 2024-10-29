#!/usr/bin/python3

import unittest
from models.amenity import Amenity

################################
#chepe@Ariel: besides BaseModel lets use this one to test out the
#workflow and approach we're gonna use to implement testing for both
#bd and file storage modes
################################

class TestAmenityFile(unittest.TestCase):

    def test_amenity__init__(self):
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.name, "")

    def test_property_name(self):
        pass

class TestAmenityDB(unittest.TestCase):

    def test_amenity__init__success(self):
        pass

    def test_amenity__init__failure(self):
        pass

    def test_property_name(self):
        pass

if __name__ == "__main__":
    unittest.main()

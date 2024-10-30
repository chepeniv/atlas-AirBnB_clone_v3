#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel, Base
import os

################################
# chepe@Ariel: besides BaseModel lets use this one to test out the
# workflow and approach we're gonna use to implement testing for both
# bd and file storage modes
################################

class TestAmenityFile(unittest.TestCase):

    def test_amenity__init__(self):
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.name, "")

    # Ariel@chepe this file is where I wrote tests for
    # Ariel@self come back to once it clicks
    def test_property_name(self):
        self.assertEqual(Amenity.name, "")

    # setup amenity before testing
    def setUp(self):
        self.amenity = Amenity("")

    # cleans up after setup
    def tearDown(self):
        self.amenity.dispose()

    # test to see if amenity inherits from base and basemodel
    def test_amenity_inherit(self):
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity, Base)

class TestAmenityDB(unittest.TestCase):

    # setup environment for db
    @classmethod
    def setUpClass(cls):
        os.environ['HBNB_TYPE_STORAGE'] = 'db'

    def test_amenity__init__success(self):
        pass

    def test_amenity__init__failure(self):
        pass

    def test_property_name(self):
        pass

if __name__ == "__main__":
    unittest.main()

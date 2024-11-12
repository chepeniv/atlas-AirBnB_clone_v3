#!/usr/bin/python3

import unittest
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models import storage, storage_type

################################
# chepe@Ariel: besides BaseModel lets use this one to test out the
# workflow and approach we're gonna use to implement testing for both
# bd and file storage modes
################################



@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
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
        storage.delete(self.amenity)

    # test to see if amenity inherits from base and basemodel
    def test_amenity_inherit(self):
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity, Base)

    # Ariel@Chepe don't know if it's truly necessary but its another test idea
    def test_amenity_many_to_many(self):
        # write test here
        pass
@unittest.skipUnless(storage_type == 'db', "Tests designed only for DBStorage")
class TestAmenityDB(unittest.TestCase):
    """Amenity DB tests"""
    def setUp(self):
        """Setup a new User instance before each test"""
        self.amenity = Amenity(name="Chair")
        storage.new(self.amenity)
        storage.save()

    def tearDown(self):
        """Teardown of all User instances after each test"""
        storage.delete(self.amenity)
        storage.save()

    def test_amenity_instance_in_storage(self):
        """Test that the Amenity instance is stored in the database"""
        key = "Amenity." + self.amenity.id
        self.assertIn(key, storage.all())

    def test_amenity_name_in_storage(self):
        """Test that the Amenity instance in storage has the correct name"""
        key = "Amenity." + self.amenity.id
        self.assertEqual(storage.all()[key].name, "Chair")

    def test_amenity_retrieval_by_id(self):
        """Test retrieval of the Amenity from storage by its ID"""
        amenity_from_storage = storage.all().get("Amenity." + self.amenity.id)
        self.assertIsNotNone(amenity_from_storage)

    def test_amenity_name_type(self):
        """Test that the name attribute is a string"""
        self.assertEqual(type(self.amenity.name), str)

    def test_amenity_name_value(self):
        """Test that the name matches the expected value"""
        self.assertEqual(self.amenity.name, "Chair")

if __name__ == "__main__":
    unittest.main()

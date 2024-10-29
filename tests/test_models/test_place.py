#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlaceFile(unittest.TestCase):

    def test_place__init__(self):
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place__tablename__(self):
        pass

    def test_place_city_id(self):
        pass

    def test_place_user_id(self):
        pass

    def test_place_name(self):
        pass

    def test_place_description(self):
        pass

    def test_place_number_rooms(self):
        pass

    def test_place_number_bathrooms(self):
        pass

    def test_place_max_guest(self):
        pass

    def test_place_price_by_night(self):
        pass

    def test_place_latitude(self):
        pass

    def test_place_longitude(self):
        pass

    def test_place_reviews(self):
        pass

class TestPlaceDB(unittest.TestCase):

    def test_place__init__success(self):
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_city__init__failure(self):
        pass

    def test_place__tablename__(self):
        pass

    def test_place_city_id(self):
        pass

    def test_place_user_id(self):
        pass

    def test_place_name(self):
        pass

    def test_place_description(self):
        pass

    def test_place_number_rooms(self):
        pass

    def test_place_number_bathrooms(self):
        pass

    def test_place_max_guest(self):
        pass

    def test_place_price_by_night(self):
        pass

    def test_place_latitude(self):
        pass

    def test_place_longitude(self):
        pass

    def test_place_reviews(self):
        pass

if __name__ == "__main__":
    unittest.main()

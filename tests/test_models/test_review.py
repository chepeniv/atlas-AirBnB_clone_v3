#!/usr/bin/python3

import unittest
from models.review import Review

class TestReviewFile(unittest.TestCase):

    def test_review__init__(self):
        new_rev = Review()
        self.assertEqual(new_rev.place_id, "")
        self.assertEqual(new_rev.user_id, "")
        self.assertEqual(new_rev.text, "")

    def test_review_text(self):
        pass

    def test_review_place_id(self):
        pass

    def test_review_user_id(self):
        pass

class TestReviewDB(unittest.TestCase):

    def test_review__init__success(self):
        pass

    def test_review__init__fail(self):
        pass

    def test_review_text(self):
        pass

    def test_review_place_id(self):
        pass

    def test_review_user_id(self):
        pass

if __name__ == "__main__":
    unittest.main()


#!/usr/bin/python3

import unittest, os
from models.state import State

class TestStateFile(unittest.TestCase):

    def test_state__init__(self):
        new_state = State()
        self.assertEqual(new_state.name, "")

    def test_state_name(self):
        pass

    def test_state_cities(self):
        pass

class TestStateDB(unittest.TestCase):

    def test_state__init__success(self):
        pass

    def test_state__init__fail(self):
        pass

    def test_state_name(self):
        pass

    def test_state_cities(self):
        pass

if __name__ == "__main__":
    unittest.main()

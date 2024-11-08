#!/usr/bin/python3

import unittest, os
from models.state import State
from models import storage, storage_type


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
class TestStateFile(unittest.TestCase):

    def setUp(self):
        self.state = State("")

    def test_state__init__(self):
        new_state = State()
        self.assertEqual(new_state.name, "")

    def test_state_name(self):
        state = State()
        state.name = ""
        self.assertEqual(state.name, "")

    def tearDown(self):
        storage.delete(self.state)

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

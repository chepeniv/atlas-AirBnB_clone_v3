#!/usr/bin/python3

import unittest
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


@unittest.skipUnless(storage_type == 'db', "Tests designed only for DBStorage")
class TestStateDB(unittest.TestCase):

    def setUp(self):
        """Setup a new State instance before each test"""
        self.state = State(name="Test_State")
        storage.new(self.state)
        storage.save()

    def tearDown(self):
        """Clean up the State instance after each test"""
        storage.delete(self.state)
        storage.save()

    def test_name(self):
        """tests that the name exists and matches"""
        self.assertEqual(type(self.state), State)
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(self.state.name, "Test_State")

    def test_state_in_storage(self):
        """tests that the instance is in the database"""
        self.assertIn("State.{}".format(self.state.id), storage.all())

if __name__ == "__main__":
    unittest.main()

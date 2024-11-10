#!/usr/bin/python3

import unittest
import os
from datetime import datetime
from uuid import uuid4
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User


# def setUpModule():
#     # runs at the start of the module
#     pass

# def tearDownModule():
#     # runs at the end of the module
#     pass


class TestFileStorage(unittest.TestCase):
    # __init__
    # new -- assert on __objects
    # save -- assert on file.json
    # reload -- assert on __objects, case file exist, file not exist
    # delete -- assert on __objects, case object not exist, object exist
    # close -- calls reload
    # construct_key -- assert on return

    def setUp(self):
        self.storage.all().clear()
        self.storage.save()
        self.storage.reload()

    # def tearDown():
    #     pass

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.json_file = "file.json"
        # if os.path.exists(cls.json_file):
        #     os.remove(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.json_file):
            os.remove(cls.json_file)

    def test_fs_count_empty(self):
        items = self.storage.all().items()
        items_count = len(items)
        self.assertEqual(items_count, 0)
        self.assertEqual(self.storage.count(), 0)

    def test_fs_count_class(self):
        self.assertEqual(self.storage.count(State), 0)
        self.assertEqual(self.storage.count(City), 0)
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(City())
        self.storage.new(City())
        self.storage.new(City())
        self.assertEqual(self.storage.count(State), 4)
        self.assertEqual(self.storage.count(City), 3)

    def test_fs_count_all(self):
        self.assertEqual(self.storage.count(), 0)
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(City())
        self.storage.new(City())
        self.storage.new(City())
        self.storage.new(User())
        self.storage.new(User())
        self.assertEqual(self.storage.count(), 9)

    def test_fs_get_no_object(self):
        self.assertIsNone(self.storage.get(State, "invalid_id"))
        self.storage.new(State)
        self.assertIsNone(self.storage.get(State, "invalid_id"))

    def test_fs_get_object(self):
        new_state = State()
        self.storage.new(new_state)
        values_state = self.storage.all().values()
        values_state = list(values_state)
        values_state = values_state[0]
        get_state = self.storage.get(State, values_state.id)
        self.assertIsInstance(get_state, State)
        self.assertEqual(get_state, values_state)

        self.storage.all().clear()

        new_city = City()
        self.storage.new(new_city)
        values_city = self.storage.all().values()
        values_city = list(values_city)
        values_city = values_city[0]
        get_city = self.storage.get(City, values_city.id)
        self.assertIsInstance(get_city, City)
        self.assertEqual(get_city, values_city)


    def test_fs_properties(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.storage.all().clear()
        self.assertEqual(self.storage.all(), {})

    def test_fs_all(self):
        self.assertIsNotNone(self.storage.all())

    def test_fs_new(self):
        time = datetime.now().isoformat()
        base_id = str(uuid4())
        kwargs = {'id': base_id, 'created_at': time, 'updated_at': time}

        new = BaseModel(**kwargs)
        key = self.storage.construct_key(new)

        self.assertNotIn(key, self.storage.all().keys())
        self.storage.new(new)
        self.assertIn(key, self.storage.all().keys())

    def test_fs_save(self):
        with open(self.json_file, 'r') as json_file:
            old_json = json_file.read()

        self.storage.new(State())
        self.storage.save()

        with open(self.json_file, 'r') as json_file:
            new_json = json_file.read()

        self.assertNotEqual(old_json, new_json)

    def test_fs_reload(self):
        new = State()
        new.save()

        old_state = self.storage.all().keys()
        old_state = list(old_state)

        self.storage.all().clear()
        clear_state = self.storage.all().keys()
        clear_state = list(clear_state)

        self.assertNotEqual(clear_state, old_state)
        self.storage.reload()
        new_state = self.storage.all().keys()
        new_state = list(new_state)
        self.assertEqual(new_state, old_state)


if __name__ == '__main__':
    unittest.main()

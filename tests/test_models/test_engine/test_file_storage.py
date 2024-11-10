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
    # additional test
    # __init__
    # new -- assert on __objects
    # save -- assert on file.json
    # reload -- assert on __objects, case file exist, file not exist
    # delete -- assert on __objects, case object not exist, object exist
    # close -- calls reload
    # construct_key -- assert on return

    def setUp():
        json_file = open(self.json_file, "w")
        json_file.write("")
        json_file.close()
        self.storage.reload()

    # def tearDown():
    #     pass

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.json_file = "file.json"
        if os.path.exists(cls.json_file):
            os.remove(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.json_file):
            os.remove(cls.json_file)

    def test_fs_count_empty():
        # assert self.storage.__objects is empty
        # assert self.storage.count() is 0
        # assert both cases true with variables
        pass

    def test_fs_count_class():
        # create 4 states
        # create 3 cities
        # assert self.storage.count(State) == 4
        # assert self.storage.count(City) == 3
        pass

    def test_fs_count_all():
        # create 4 states
        # create 3 cities
        # create 2 users
        # assert self.storage.count() == 9
        pass

    def test_fs_get_no_object():
        # assert self.storage.__objects is empty
        # assert self.storage.get(State, id_false) is None
        # self.storage.new(State)
        # assert self.storage.get(State, id_false) is None
        pass

    def test_fs_get_object():
        # create a State
        # create a City
        # assert self.storage.get(State, id_true) is state
        # assert self.storage.get(City, id_true) is city
        # assert on return
        pass

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

        new = BaseModel()
        self.storage.save()

        with open(self.json_file, 'r') as json_file:
            new_json = json_file.read()

        self.assertNotEqual(old_json, new_json)

    def test_fs_reload(self):
        new = BaseModel()
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

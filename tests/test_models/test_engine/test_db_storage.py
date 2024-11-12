#!/usr/bin/python3

# import unittest
# import os
# from datetime import datetime
# from uuid import uuid4
# from models.engine.db_storage import DBStorage
# from models.state import State
# from models.city import City
# from models.user import User

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}
# def setUpModule():
#     HBNB_ENV=test \
#     HBNB_MYSQL_USER=hbnb_test \
#     HBNB_MYSQL_PWD=hbnb_test_pwd \
#     HBNB_MYSQL_HOST=localhost \
#     HBNB_MYSQL_DB=hbnb_test_db \
#     HBNB_TYPE_STORAGE=db \
#     runs at the start of the module
#     pass

# def tearDownModule():
#     runs at the end of the module
#     pass

# storage_type = os.environ.get('HBNB_TYPE_STORAGE', 'file')
# db = os.environ.get('HBNB_ENV', 'test')

# Commented entire class because it's written for file_storage
# class TestFileStorage(unittest.TestCase):
#     # assert a current state of item
#     # execute action,
#     # validate result of action on item
#     # to test if it works, it’s better to isolate from the system

#     # get the number of current records in the table states
#     # execute the console command: create State name="California"
#     # get  the number of current records in the table states
#     # if the difference is +1 => test passed

#     # __init__
#     # new -- assert on __objects
#     # save -- assert on file.json
#     # reload -- assert on __objects, case file exist, file not exist
#     # delete -- assert on __objects, case object not exist, object exist
#     # close -- calls reload
#     # construct_key -- assert on return

#     def setUp(self):
#         self.storage.all().clear()
#         self.storage.save()
#         self.storage.reload()

#     # def tearDown():
#     #     pass

#     @classmethod
#     def setUpClass(cls):
#         cls.storage = FileStorage()
#         cls.json_file = "file.json"
#         # if os.path.exists(cls.json_file):
#         #     os.remove(cls.json_file)

#     @classmethod
#     def tearDownClass(cls):
#         if os.path.exists(cls.json_file):
#             os.remove(cls.json_file)

#     def test_fs_count_empty(self):
#         items = self.storage.all().items()
#         items_count = len(items)
#         self.assertEqual(items_count, 0)
#         self.assertEqual(self.storage.count(), 0)

#     def test_fs_count_class(self):
#         self.assertEqual(self.storage.count(State), 0)
#         self.assertEqual(self.storage.count(City), 0)
#         self.storage.new(State())
#         self.storage.new(State())
#         self.storage.new(State())
#         self.storage.new(State())
#         self.storage.new(City())
#         self.storage.new(City())
#         self.storage.new(City())
#         self.assertEqual(self.storage.count(State), 4)
#         self.assertEqual(self.storage.count(City), 3)

#     def test_fs_count_all(self):
#         self.assertEqual(self.storage.count(), 0)
#         self.storage.new(State())
#         self.storage.new(State())
#         self.storage.new(State())
#         self.storage.new(State())
#         self.storage.new(City())
#         self.storage.new(City())
#         self.storage.new(City())
#         self.storage.new(User())
#         self.storage.new(User())
#         self.assertEqual(self.storage.count(), 9)

#     def test_fs_get_no_object(self):
#         self.assertIsNone(self.storage.get(State, "invalid_id"))
#         self.storage.new(State())
#         self.assertIsNone(self.storage.get(State, "invalid_id"))

#     def test_fs_get_object(self):
#         new_state = State()
#         self.storage.new(new_state)
#         values_state = self.storage.all().values()
#         values_state = list(values_state)
#         values_state = values_state[0]
#         get_state = self.storage.get(State, values_state.id)
#         self.assertIsInstance(get_state, State)
#         self.assertEqual(get_state, values_state)

#         self.storage.all().clear()

#         new_city = City()
#         self.storage.new(new_city)
#         values_city = self.storage.all().values()
#         values_city = list(values_city)
#         values_city = values_city[0]
#         get_city = self.storage.get(City, values_city.id)
#         self.assertIsInstance(get_city, City)
#         self.assertEqual(get_city, values_city)

#     def test_fs_properties(self):
#         self.assertEqual(self.storage._FileStorage__file_path, "file.json")
#         self.storage.all().clear()
#         self.assertEqual(self.storage.all(), {})

#     def test_fs_all(self):
#         self.assertIsNotNone(self.storage.all())

#     def test_fs_new(self):
#         time = datetime.now().isoformat()
#         base_id = str(uuid4())
#         kwargs = {'name': 'Name', 'id': base_id,
#                   'created_at': time, 'updated_at': time}

#         new = State(**kwargs)
#         key = self.storage.construct_key(new)

#         self.assertNotIn(key, self.storage.all().keys())
#         self.storage.new(new)
#         self.assertIn(key, self.storage.all().keys())

#     def test_fs_save(self):
#         with open(self.json_file, 'r') as json_file:
#             old_json = json_file.read()

#         self.storage.new(State())
#         self.storage.save()

#         with open(self.json_file, 'r') as json_file:
#             new_json = json_file.read()

#         self.assertNotEqual(old_json, new_json)

#     def test_fs_reload(self):
#         new = State()
#         new.save()

#         old_state = self.storage.all().keys()
#         old_state = list(old_state)

#         self.storage.all().clear()
#         clear_state = self.storage.all().keys()
#         clear_state = list(clear_state)

#         self.assertNotEqual(clear_state, old_state)
#         self.storage.reload()
#         new_state = self.storage.all().keys()
#         new_state = list(new_state)
#         self.assertEqual(new_state, old_state)

class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

if __name__ == '__main__':
    unittest.main()

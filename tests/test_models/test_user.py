#!/usr/bin/python3


import unittest, os
from models.user import User
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.test_file = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_user__init__(self):
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_user_to_dict(self):
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")

    def test_user_save_reload(self):
        new_user = User()
        old_updated_at = new_user.updated_at
        key = f"User.{new_user.id}"

        new_user.save()
        self.storage.reload()
        self.assertNotEqual(old_updated_at, new_user.updated_at)
        self.assertIn(key, self.storage.all())

    def test_user_email(self):
        # Ariel@Chepe I put the following code in comments because it was the
        # first thing I saw before the one I have now
        # Let me know if either are even correct
        # self.user = User(email="") not right?
        self.assertEqual(User.email, "")

    def test_user_password(self):
        # self.user = User(password="")
        self.assertEqual(User.password, "")

    def test_user_first_name(self):
        # self.user = User(first_name="")
        self.assertEqual(User.first_name, "")
        
    def test_user_last_name(self):
        # self.user = User(last_name="")
        self.assertEqual(User.last_name, "")
        
    def test_user_places(self):
        pass

    def test_user_reviews(self):
        pass

class TestUserDB(unittest.TestCase):

    def test_user__init__success(self):
        pass

    def test_user__init__fail(self):
        pass

    def test_user_email(self):
        pass

    def test_user_password(self):
        pass

    def test_user_first_name(self):
        pass

    def test_user_last_name(self):
        pass

    def test_user_places(self):
        pass

    def test_user_reviews(self):
        pass

if __name__ == '__main__':
    unittest.main()

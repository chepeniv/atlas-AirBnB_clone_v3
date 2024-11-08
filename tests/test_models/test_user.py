#!/usr/bin/python3


import unittest, os
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage_type, storage


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
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


@unittest.skipUnless(storage_type == 'db', "Tests designed only for DBStorage")
class TestUserDB(unittest.TestCase):

    def setUp(self):
        """Setup a new User instance before each test"""
        self.user = User(email="a@b.com", password="password",
                         first_name="John", last_name="Roe")
        storage.new(self.user)
        storage.save()

    def tearDown(self):
        """Clean up the User instance after each test"""
        storage.delete(self.user)
        storage.save()

    def test_first_name_type(self):
        """Test that first_name is a string"""
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name_type(self):
        """Test that last_name is a string"""
        self.assertEqual(type(self.user.last_name), str)

    def test_email_type(self):
        """Test that email is a string"""
        self.assertEqual(type(self.user.email), str)

    def test_password_type(self):
        """Test that password is a string"""
        self.assertEqual(type(self.user.password), str)

    def test_first_name_value(self):
        """Test that first_name can be set"""
        self.assertEqual(self.user.first_name, "John")

    def test_last_name_value(self):
        """Test that last_name can be set"""
        self.assertEqual(self.user.last_name, "Roe")

    def test_email_value(self):
        """Test that email can be set"""
        self.assertEqual(self.user.email, "a@b.com")

    def test_password_value(self):
        """Test that password can be set"""
        self.assertEqual(self.user.password, "password")

    def test_user_instance_in_storage(self):
        """Test that the User instance is stored in the database"""
        storage.new(self.user)
        storage.save()
        key = "User." + self.user.id
        self.assertIn(key, storage.all())

    def test_user_retrieval_by_id(self):
        """Test retrieval of the user from storage by its ID"""
        storage.new(self.user)
        storage.save()
        user_from_storage = storage.all().get("User." + self.user.id)
        self.assertIsNotNone(user_from_storage)

    def test_user_retrieved_has_correct_id(self):
        """Test that the retrieved user's ID matches the original ID"""
        storage.new(self.user)
        storage.save()
        user_from_storage = storage.all().get("User." + self.user.id)
        self.assertEqual(user_from_storage.id, self.user.id)

    def test_user_retrieved_has_correct_first_name(self):
        """Test that the retrieved user's
        first_name matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.first_name, "John")

    def test_user_retrieved_has_correct_last_name(self):
        """Test that the retrieved user's
        last_name matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.last_name, "Roe")

    def test_user_retrieved_has_correct_email(self):
        """Test that the retrieved user's email matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.email, "a@b.com")

    def test_user_retrieved_has_correct_password(self):
        """Test that the retrieved user's
        password matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.password, "password")

if __name__ == '__main__':
    unittest.main()

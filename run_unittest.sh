clear;

HBNB_ENV=test \
HBNB_MYSQL_USER=hbnb_test \
HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_DB=hbnb_test_db \
HBNB_TYPE_STORAGE=db \
python3 -m unittest discover -v 1>unittest.log 2>&1

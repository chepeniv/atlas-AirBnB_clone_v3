# run with sudo

# rm json.file;

cat setup_mysql_dev.sql | mysql;

HBNB_MYSQL_USER=hbnb_dev
HBNB_MYSQL_PWD=hbnb_dev_pwd
HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db
HBNB_TYPE_STORAGE=db

tests/console_cmds.sh | ./console.py &> tests/console_err

cat tests/mysql_cmds.sql | mysql

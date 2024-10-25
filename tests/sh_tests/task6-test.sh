# run with sudo

# rm json.file;

export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_TYPE_STORAGE=db

cat setup_mysql_dev.sql | mysql;

tests/console_cmds.sh | ./console.py &> tests/console_err

cat tests/mysql_cmds.sql | mysql

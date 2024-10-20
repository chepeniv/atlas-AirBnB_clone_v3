# tasks

## task 0 - fork me if you can

common questions when working with a prexisting codebase:
- who wrote it 
- how does it work
- what are the unittest
- where is it stored
- why is it written the way that it is

although tempting one should refrain from rewritting everything.
regardless, trust should not be granted automatically.
always view it with a critical eye

whether the repo is forked or cloned, update the name as well as the README.
do not remove the original authors.

## task 1 - bug free

regardless of the storage engine used, all unittest must pass without errors

running the test with predefined environment variables
```bash
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
```
due to their irrelevance, some test might need to be skipped with the `skipif` [feature](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)

for any skipped test, be sure to write a new one

### testing with mysql

create a specific database for testing. 

(1) assert the current state, (2) execute an action, and (3) validate the state changes performed by the action

when testing various components functionality it is better to do so in isolation

## task 2 - console improvements

update `def do_create(self, arg)` of the command interpreter `console.py` to allow for 
object creation with given parameters

command syntax : `cerate <class> <param1> <param2> <param3> ...`
parameter syntax : `<key>=<value>`
value syntax : `"<value>"`
	- double quotes within can be escaped with `\`
	- values passed will be deliniated by underscores. internally, replace theses with spaces
	- floats must contain dots otherwise an integer will be the default interpretation
uninterpretable parameters must be skipped

in the checker, this will be tested with the original `FileStorage` engine

FILE: `console.py`, `models/`, and `tests/`

## task 3 - mysql setup development

write an sql script to prepare a mysql server for the project

- database : `hbnb_dev_hb`
- user : `hbnb_dev` in `localhost`
- password : `hbnb_dev_pwd`
- the new user should have **all** privileges to the new db **only**
- add the `SELECT` privilege for the new user on `performance_schema`
- if either the db or the user already exist, the script should not fail

## task 4 - mysql setup dev

write an sql script to prepare a mysql server for the project

- database : `hbnb_test_hb`
- user : `hbnb_test` in `localhost`
- password : `hbnb_test_pwd`
- the new user should have **all** privileges to the new db **only**
- add the `SELECT` privilege for the new user on `performance_schema`
- if either the db or the user already exist, the script should not fail

## task 5 - delete object

update `FileStorage` in `model/engine/file_storage.py`
add a new public instance method : `def delete(self, obj=None):` that deletes `obj` from `__objects` if it exist within. if `obj` is `None` don't do anything

update the prototype `def all(self)` to `def all(self, cls=None)` that returns a list of objects of the type of class determined by `cls` optional filter

FILE: `models/engine/file_storage.py`

## task 6 - dbstorage - states nad cities

## task 7 - dbstorage - user

## task 8 - dbstorage - place

## task 9 - dbstorage - review

## task 10 - dbstorage - amenity


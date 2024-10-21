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

## task 6 - dbstorage - states and cities

here we will transition from `FileStorage` to `DBStorage`.

it is not adviced that a service work with multiple backend storage systems
simultaneously. but it is common to have the storage layer abstracted in order to
be able to swap out the implementation as need be

add class attributes to `SQLStorage` with values for description and mapping to the 
database. modifying these values, or adding or removing attributes to the model will
force you to delete and reconstruct the database. although not optimal, it's fine 
for development purpsoses.

### steps

#### update : `models/base_model.py:BaseModel`

create `Base = declarative_base()` before `class BaseMode`.

- `BaseModel`: 
	- `id` - 60 char, unique, not null, primary key
	- `created_at` - datetime, not null, default is `datetime.utcnow()`
	- `updated_at` - datetime, not null, default is `datetime.utcnow()`
- move `models.storage.new(self)` from `def __init__(self, *args, **kwargs):` over to `def save(self):` and call it just before `model.storage.save()`
- in `def __init__(self, *args, **kwargs)` use `**kwargs` to create instance attributes
	- example: `kwargs={ 'name': 'value' }` --> `self.name = 'value'`
- update `to_dict()`
	- remove `_sa_instance_state` from the dictionary recturned if it exist
- add the public instance method `def delete(self)` to remove the current instance from `models.storage` by calling the mothod `delete`

#### update : `models/city.py:City`

- `City` inherits from `BaseModel` and then `Base` (order is important)
- `City`:
	- `__tablename__` represents the table name `cities`
	- `name` - string of 128 chars, can't be null
	- `state_id` 60 char, not null, foreign key to `state.id`

#### update : `models/state.py:State`

- `State` inherits from `BaseModel` and then `Base` (order is important)
- `State`:
	- `__tablename__` represents the table name `states`
	- `name` - string of 128 chars, can't be null
	- `state_id` 60 char, not null, foreign key to `state.id`
	- in `DBStorage` :
		- `cities` attribute must represent a relationship with class `Cities`
		- if a `State` object is deleted, then all linked `City` must be deleted as well
		- the reference from a `City` object to it's `State` should be named `state`
	- in `FileStorage` :
		- the getter attribute `cities` should return a list of `City` instances with `state_id` equal to the current `State.id` -- the relationship between `State` and `City` in `FileStorage`

#### new engine: `model/engine/db_storage.py:DBStorage`

- private class attributes :
	- `__engine` set to `None`
	- `__session` set to `None`
- public instance methods :
	- `__init__(self)` :
		- create engine `self.__engine`
		- link this engine to the mysql database and user : `hbnb_dev` and `hbnb_dev_db`:
			- dialect : `mysql` ; driver `mysqldb`
		- retrieve values from the given environment variables :
			- mysql user from `HBNB_MYSQL_USER`
			- mysql password from `HBNB_MYSQL_PWD`
			- mysql host from `HBNB_MYSQL_HOST` (=`localhost`)
			- mysql database from `HBNB_MYSQL_DB`
		- set the option `pool_pre_ping=True` when calling `create_engine`
		- drop all tables if `HBNB_ENV` is equal to `test`
	- `all(self, cls=None)`:
		- query the current database session `self.__session` to extract all objects dependant on the class name `cls`


	- `new(self, obj)`
	- `save(self)`
	- `delete(self, obj=None)`
	- `reload(self)`

## task 7 - dbstorage - user

## task 8 - dbstorage - place

## task 9 - dbstorage - review

## task 10 - dbstorage - amenity


# delegation

add more subtask for any issues that arise

## priority

- [ ] reintegrate `file_storage.py` - **chepe**
	- [ ] implement `create Class key1="value1" key2="value2" ...` format

- [ ] task1 - bug free - **Ariel**, **chepe**
	- reference: [feature](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)

----

## in progress

- [~] task7 - dbstorage user - **Ariel**

- [ ] task8 - dbstorage place - **Ariel**
	- [ ] add the required columns
	- [ ] contrary to instruction: don't rename `user_id` to `user`
	- [ ] contrary to instruction: don't rename `city_id` to `cities`
	- [ ] `models/user.py:User`
		- [ ] `places = relationship('Place', cascade='all, delete')`
	- [ ] `models/city.py:City`
		- [ ] `places = relationship('Place', cascade='all, delete')`

- [ ] task9 - dbstorage review - **Ariel**
	- [ ] add the required columns
	- [ ] contrary to instruction: don't rename `user_id` to `user`
	- [ ] contrary to instruction: don't rename `place_id` to `place`
	- [ ] `models/user.py:User`
		- [ ] `reviews = relationship('Review', cascade='all, delete')`
	- [ ] `models/place.py:Place`
		- [ ] check out how state is written for this one

- [ ] task10 - dbstorage amenity - **Ariel**, **chepe**
	- [ ] add the required columns
	- [ ] `models/place.py:Place` - **chepe**
		- [ ] create new table `place_amenity`
		- [ ] update class

----

## extra

### console

- [ ] add `do_models` -- list all models available
- [ ] implement `destroy all` -- for convenience

----

## completed

- [x] task0 - fork

- [x] task2 - console improvements - **chepe**

- [x] task3 - mysql setup dev - **Ariel**

- [x] task4 - mysql setup test - **Ariel**

- [x] task5 - delete object - **chepe**

- [x] task6 - dbstorage states and cities - **chepe**
	- [x] update `models/__init__.py`
	- [x] update `models/base_model.py`
		- [x] `kwargs={ 'name': 'value' }` --> `self.name = 'value'`
	- [x] create new engine `models/engine/db_storage.py`
		- [x] `__init__(self)`
		- [x] `all(self, cls=None)`
		- [x] `new(self, obj)`
		- [x] `save(self)`
		- [x] `reload(self)`
		- [x] `delete(self, obj=None)`
	- [x] update `models/state.py`
		- [x] implement storage-dependent behavior
	- [x] update `models/city.py`
	- [x] get code to work
	- [x] fix bugs
		- [x] fixed `_sa_instance_state` issue

- [x] `console_util.py` - **chepe**
- [x] `console.py`

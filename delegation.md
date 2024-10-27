# delegation

add more subtask for any issues that arise

- [x] task0 - fork

- [ ] task1 - bug free - **Ariel**, **chepe**
	- reference: [feature](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures)

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

- [ ] task7 - dbstorage user - **Ariel**

- [ ] task8 - dbstorage place - **Ariel**

- [ ] task9 - dbstorage review - **Ariel**

- [ ] task10 - dbstorage amenity - **Ariel**, **chepe**

- [x] `console_util.py` - **chepe**

- [ ] `console.py`
	- [ ] note: there might need to be some work done here

- [ ] `file_storage.py` - **chepe**
	- [ ] get it to work again

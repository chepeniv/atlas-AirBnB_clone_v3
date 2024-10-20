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

## task 3 - mysql setup development

## task 4 - mysql setup dev

## task 5 - delete object

## task 6 - dbstorage - states nad cities

## task 7 - dbstorage - user

## task 8 - dbstorage - place

## task 9 - dbstorage - review

## task 10 - dbstorage - amenity


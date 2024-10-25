#!/bin/bash

# echo "select valid mode: 'dev' or 'test' :"
export HBNB_DB_MODE=dev
export HBNB_ROOT=~/Learning/AtlasSchool/Sandbox/atlas-AirBnB_clone_v2/
export HBNB_SH_TEST_DIR=$HBNB_ROOT/tests/sh_tests/
export HBNB_MYSQL_USER=hbnb_$HBNB_DB_MODE
export HBNB_MYSQL_PWD=hbnb_$HBNB_DB_MODE\_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_$HBNB_DB_MODE\_db
export HBNB_TYPE_STORAGE=db

sudo python3 console.py


#!/bin/bash

export HBNB_DB_MODE=dev;
export HBNB_ROOT=~/Learning/AtlasSchool/Sandbox/atlas-AirBnB_clone_v2/;
export HBNB_SH_TEST_DIR=$HBNB_ROOT/tests/sh_tests/;

HBNB_MYSQL_USER=hbnb_$HBNB_DB_MODE HBNB_MYSQL_PWD=hbnb_$HBNB_DB_MODE\_pwd HBNB_MYSQL_HOST=localhost; HBNB_MYSQL_DB=hbnb_$HBNB_DB_MODE\_db HBNB_TYPE_STORAGE=db ./console.py


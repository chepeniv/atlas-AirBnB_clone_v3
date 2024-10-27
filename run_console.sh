#!/bin/bash

clear;
export HBNB_DB_MODE=dev;
export HBNB_SH_TEST_DIR=$PWD/tests/sh_tests/;

HBNB_MYSQL_USER=hbnb_$HBNB_DB_MODE HBNB_MYSQL_PWD=hbnb_$HBNB_DB_MODE\_pwd HBNB_MYSQL_HOST=localhost; HBNB_MYSQL_DB=hbnb_$HBNB_DB_MODE\_db HBNB_TYPE_STORAGE=db ./console.py


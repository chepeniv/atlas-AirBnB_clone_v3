-- Ariel: create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--Ariel:  create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_pwd'
-- Ariel: grant all priveleges only on hbnb_dev_db
GRANT ALL PRIVELEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
-- Ariel: grant select priveleges only on performance_schema database
GRANT SELECT ON 'performance_schema' TO 'hbnb_dev'@'localhost';
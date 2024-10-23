-- Ariel create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--Ariel:  create user if it doesn't exist; inserted WITH to autheniticate
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH authorization_plugin BY 'hbnb_dev_pwd';
-- Ariel: grant all priveleges only on hbnb_dev_db
GRANT ALL PRIVELEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Ariel: grant select priveleges only on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- push priveleges
FLUSH PRIVELEGES;
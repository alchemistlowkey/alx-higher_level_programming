-- A script that creates a user and a database
CREATE USER
IF NOT EXISTS user_0d_2@localhost
	IDENTIFIED BY "user_0d_2_pwd";

CREATE DATABASE
IF NOT EXISTS hbtn_0d_2;

GRANT SELECT ON hbtn_0d_2.* 
TO user_0d_2@localhost;

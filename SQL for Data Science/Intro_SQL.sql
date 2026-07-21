CREATE DATABASE Intro_SQL

USE Intro_SQL;

DROP TABLE Students;

CREATE TABLE Students
(
student_id int,
student_name varchar(50) NOT NULL,
age int,
gender varchar(1),
location varchar(100)
)

SELECT * FROM Students;

INSERT INTO Students VALUES (1,'Maya',23,'F','China')
INSERT INTO Students VALUES (2,null,23,'F','China')   #error



CREATE TABLE dep
(
depid INT NOT NULL PRIMARY KEY,
depname VARCHAR(100),
depadd VARCHAR(200)
) 

CREATE TABLE emp
(
empid INT,
empname VARCHAR(100),
empadd VARCHAR(200),
depid INT,
PRIMARY KEY (empid),
FOREIGN KEY (depid) REFERENCES dep(depid)
)





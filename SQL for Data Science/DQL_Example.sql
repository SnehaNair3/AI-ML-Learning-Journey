USE Intro_sql;

SHOW TABLES;

CREATE TABLE empinfo
(
first_name VARCHAR(50),
last_name VARCHAR(50),
id INT NOT NULL,
age INT,
city VARCHAR(50),
state VARCHAR(50),
PRIMARY KEY(id)
);



SELECT * FROM empinfo;

INSERT INTO empinfo VALUES ('John','Philip',1,34,'Payson','Arizona');
INSERT INTO empinfo VALUES ('Mary','Joseph',2,37,'Kochi','Kerala');
INSERT INTO empinfo VALUES ('Eric','Edwin',3,23,'Bangalore','Karnataka');



SELECT first_name, last_name FROM empinfo;
SELECT first_name AS firstName, last_name AS lastName FROM empinfo;

SELECT COUNT(*) FROM empinfo;
SELECT COUNT(id) FROM empinfo;
SELECT COUNT(id) AS record_count FROM empinfo;

SELECT first_name,last_name,city FROM empinfo;

SELECT last_name,city,age FROM empinfo WHERE age > 30;

SELECT first_name,last_name,city,state FROM empinfo WHERE first_name LIKE 'J%';

SELECT * FROM empinfo;

SELECT first_name,last_name from empinfo WHERE last_name LIKE '%s';
SELECT first_name,last_name from empinfo WHERE last_name LIKE '%p';

SELECT first_name,last_name ,age FROM empinfo WHERE last_name LIKE '%illia%';
SELECT first_name,last_name ,age FROM empinfo WHERE last_name LIKE '%hil%';

SELECT * FROM empinfo WHERE first_name='Eric';

SELECT first_name , last_name,age FROM empinfo WHERE age > 30 and age <50;

SELECT first_name ,last_name,age FROM empinfo WHERE age=34 or age=56;
# OR
SELECT first_name,last_name,age FROM empinfo WHERE age in (34,67,23);

SELECT first_name,last_name, age FROM empinfo WHERE first_name='John' and last_name='philip' or age=45;


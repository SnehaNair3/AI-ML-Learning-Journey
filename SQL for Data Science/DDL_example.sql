USE Intro_SQL;

SHOW TABLES;

CREATE TABLE employeees
(
emp_name VARCHAR(50),
emp_id INT NOT NULL,
manager_name VARCHAR(50),
division INT,
PRIMARY KEY (emp_id)
)

SELECT * FROM employees;



# Exercise
CREATE TABLE new_emp
(
first_name VARCHAR(100),
last_name VARCHAR(100),
title VARCHAR(50),
age INT,
salary INT
)

SELECT * FROM new_emp;

# ALTER
ALTER TABLE new_emp 
ADD gender varchar(10);

ALTER TABLE new_emp 
ADD random char;

ALTER TABLE new_emp
DROP COLUMN random;



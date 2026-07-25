
USE Intro_sql;


CREATE TABLE emp_exercise
(
emp_name varchar(50),
designation varchar(100),
emp_age int ,
emp_salary float
);



INSERT INTO emp_exercise VALUES ('Jonie Weber','Secretary',28,19500.00);
INSERT INTO emp_exercise VALUES ('Posty Weber','Programmer',32,45300.00);
INSERT INTO emp_exercise VALUES ('Dirk Smith','Programmer ||',45,75020.00);
INSERT INTO emp_exercise VALUES ('Federick Manuel','Programmer ||',56,69000.00);
INSERT INTO emp_exercise VALUES ('Abin Philipose','Programmer',25,96500.00);
INSERT INTO emp_exercise VALUES ('John Jacob','Doctor',36,95000.00);
INSERT INTO emp_exercise VALUES ('Alan Turing','Secretary',38,39500.00);
INSERT INTO emp_exercise VALUES ('Joyal Dojo','Secretary',42,35500.00);
INSERT INTO emp_exercise VALUES ('Merin Jose','IT Support',31,45000.00);


SELECT * FROM emp_exercise;

SELECT * FROM emp_exercise WHERE emp_salary > 30000;

SELECT emp_name FROM emp_exercise WHERE emp_age <30;

SELECT emp_name,emp_salary FROM emp_exercise WHERE designation LIKE '%Programmer%';

SELECT * FROM emp_exercise WHERE emp_name LIKE '%ebe%';

SELECT emp_name FROM emp_exercise WHERE emp_name='Potsy';

SELECT * FROM emp_exercise WHERE emp_age > 80;

SELECT * FROM emp_exercise WHERE emp_name LIKE '%ITH';


# UPDATE
SET SQL_SAFE_UPDATES=0;
UPDATE emp_exercise SET designation='Senior Programmer' WHERE emp_name ='Dirk Smith';

UPDATE emp_exercise SET designation='Data Analyst',emp_age=27 WHERE emp_name='Abin Philipose';

UPDATE emp_exercise SET designation='Data Analyst' WHERE emp_name='Jonie Weber' and emp_age=28;

UPDATE emp_exercise SET emp_name='Jonie Williams' WHERE emp_name='Jonie Weber';
SELECT * FROM emp_exercise;

UPDATE emp_exercise SET emp_age=emp_age+1 WHERE emp_name='Dirk Smith';
SELECT * FROM emp_exercise;

UPDATE emp_exercise SET designation='Administrative Assistant' WHERE designation='Secretary';
SELECT * FROM emp_exercise;


UPDATE emp_exercise SET emp_salary=emp_salary+3500 WHERE emp_salary<30000;
SELECT * FROM emp_exercise;


UPDATE emp_exercise SET emp_salary=emp_salary+4500 WHERE emp_salary >33500;
SELECT * FROM emp_exercise;


UPDATE emp_exercise SET designation='Programmer |||' WHERE designation='Programmer ||';
SELECT * FROM emp_exercise;


UPDATE emp_exercise SET designation='Programmer ||' WHERE designation='Programmer';
SELECT * FROM emp_exercise;


DELETE FROM emp_exercise WHERE emp_name='Merin Jose' AND designation='IT Support';
SELECT * FROM emp_exercise;



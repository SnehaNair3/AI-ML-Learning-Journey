
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


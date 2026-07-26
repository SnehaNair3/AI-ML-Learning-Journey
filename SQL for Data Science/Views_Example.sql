

CREATE TABLE members
(
first_name VARCHAR(50),
last_name VARCHAR(50),
age INT,
gender VARCHAR(10),
job_title VARCHAR(50),
org_id INT
);

DROP TABLE members;

INSERT INTO members VALUES ('Diya','Mathew',23,'Female','Data Analyst',1);
INSERT INTO members VALUES ('Roshan','Thomas',34,'Male','Data Engineer',1);
INSERT INTO members VALUES ('Prisha','Guptha',25,'Female','Product Designer',1);
INSERT INTO members VALUES ('Abhay','Krishna',30,'Male','Software Engineer',1);
INSERT INTO members VALUES ('Jaison','Joseph',28,'Male','Data Scientist',1);

SELECT * FROM members;

# Table creation insead of view- takes up storage
CREATE TABLE new_members AS 
SELECT * FROM members WHERE gender='Female';

DROP TABLE new_members;

SELECT * FROM new_members;

# Creating views - doesnt take up storage
CREATE VIEW members_view AS 
SELECT * FROM members WHERE gender='Female';

DROP VIEW members_view;


SELECT * FROM members_view;


CREATE TABLE org_details
(
id INT,
org_name VARCHAR(50),
org_location VARCHAR(100),
no_members INT
);

INSERT INTO org_details VALUES (1,'UNICEF','Geneva',1000);
INSERT INTO org_details VALUES (2,'WHO','Geneva',500);
INSERT INTO org_details VALUES (3,'RBI','India',5000);
INSERT INTO org_details VALUES (4,'UN','USA',8000);

SELECT * FROM org_details;

SELECT m.first_name, m.last_name,m.job_title,o.org_name,o.org_location FROM members m, org_details o WHERE m.org_id=o.id;


CREATE VIEW mem_details AS SELECT m.first_name, m.last_name,m.job_title,o.org_name,o.org_location FROM members m, org_details o WHERE m.org_id=o.id;

SELECT * FROM mem_details;



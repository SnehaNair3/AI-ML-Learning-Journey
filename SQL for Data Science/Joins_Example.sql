CREATE DATABASE Join_SQL;

USE Join_SQL;


CREATE TABLE Customers
(
customerid INT PRIMARY KEY,
customername VARCHAR(50),
contactname VARCHAR(50),
address VARCHAR(100),
city VARCHAR(50),
postalcode VARCHAR(100),
country VARCHAR(50)
);



CREATE TABLE orders
(
orderId INT NOT NULL PRIMARY KEY,
customerId INT,
employeeId INT,
orderDate DATETIME,
shipperId INT
);


INSERT INTO Customers VALUES (1,'Joyal Jose','Maria','New York, USA','New York','12GHY','USA');
INSERT INTO Customers VALUES (2,'Christeena Jomy','Clince','Brisbane, Australia','Brisbane','35GHY','Australia');
INSERT INTO Customers VALUES (3,'Henna Mary','Diya Mathew','Nuremberg, Germany','Nuremberg','1245-U','Germany');
INSERT INTO Customers VALUES (4,'Merin Mariya','Jaison Mathew','Bangalore, India','Bnagalore','4th Block, Koramangala','India');
INSERT INTO Customers VALUES (5,'Elina Philip','Emil Mariya','London, UK','London','1565-U','UK');
INSERT INTO Customers VALUES (6,'Ann Mariya','Delna Joseph','Edinburgh, UK','Edinburgh','1565-U','UK');
INSERT INTO Customers VALUES (7,'Alice Thomas','Riya Thomas','Brussels, Belgium','Brussels','15gh-U','Belgium');
INSERT INTO Customers VALUES (8,'Clerin Jomy','Kevin Thomas','Vienna, Austria','Austria','2565-H','Austria');

SELECT * FROM customers;

INSERT INTO orders VALUES (101,201,301,'2020-12-03',401);
INSERT INTO orders VALUES (102,2,302,'2020-12-04',402);
INSERT INTO orders VALUES (103,3,303,'2020-12-03',403);
INSERT INTO orders VALUES (104,4,304,'2020-12-06',405);
INSERT INTO orders VALUES (105,5,305,'2020-12-08',408);
INSERT INTO orders VALUES (106,6,306,sysdate(),406);
INSERT INTO orders VALUES (107,7,307,sysdate()-10,407);
INSERT INTO orders VALUES (108,8,308,sysdate()-40,40);
INSERT INTO orders VALUES (109,215,311,sysdate()-40,485);
INSERT INTO orders VALUES (110,225,318,sysdate()-10,465);


SELECT * FROM orders;


# LEFT JOIN
SELECT c.customerid,c.customername,c.city,c.country,o.orderId,o.orderDate FROM Customers c 
LEFT JOIN orders o
ON c.customerid=o.customerId;


# RIGHT JOIN
SELECT c.customerid,c.customername,c.city,c.country,o.orderId,o.orderDate FROM Customers c 
RIGHT JOIN orders o
ON c.customerid=o.customerId;


#INNER JOIN
SELECT c.customerid,c.customername,c.city,c.country,o.orderId,o.orderDate FROM Customers c 
INNER JOIN orders o
ON c.customerid=o.customerId;

# OR (also called as INNER JOIN)

SELECT c.customerid,c.customername,c.city,c.country,o.orderId,o.orderDate FROM Customers c , orders o
WHERE c.customerid=o.customerId;



# OUTER JOIN
SELECT c.customerid,c.customername,c.city,c.country,o.orderId,o.orderDate FROM Customers c 
LEFT OUTER JOIN orders o
ON c.customerid=o.customerId
UNION
SELECT c.customerid,c.customername,c.city,c.country,o.orderId,o.orderDate FROM Customers c 
RIGHT OUTER JOIN orders o
ON c.customerid=o.customerId;


# CROSS JOIN
SELECT c.customerid,c.customername,c.city,c.country,o.orderId,o.orderDate FROM Customers c 
CROSS JOIN orders o
ON c.customerid=o.customerId;




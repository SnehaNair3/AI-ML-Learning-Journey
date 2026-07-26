
USE classicmodels;

SHOW TABLES;


SELECT * FROM products;

SELECT SUM(msrp), productLine FROM products GROUP BY productLine;

CREATE TABLE productLinemsrp AS
SELECT SUM(msrp),productLine FROM products GROUP BY productLine;

SELECT * FROM productLinemsrp;


SELECT a.productLine, a.* ,SUM(msrp) OVER (PARTITION BY a.productLine) AS total_msrp FROM products a;


# Row_number()
SELECT ROW_NUMBER() OVER (ORDER BY msrp) AS row_num,productLine,msrp FROM products
ORDER BY msrp;


SELECT ROW_NUMBER() OVER (ORDER BY msrp) AS row_num,productLine,msrp FROM products
ORDER BY msrp;

SELECT ROW_NUMBER() OVER (ORDER BY productLine) AS row_num,productLine,msrp FROM products
ORDER BY productLine;


SELECT COUNT(*) FROM products;



USE Intro_sql;

CREATE TABLE demo
(
var_a int
);

INSERT INTO demo VALUES (101),(102),(103),(103),(104),(105),(106),(106);

SELECT * FROM demo;

SELECT var_a,
RANK() OVER (ORDER BY var_a) AS test_ranks FROM demo;

# 5 --> 91,88,88,14,13

# Rank 1 : 91
# Rank 2 : 88
# Rank 3 : -
# Rank 4 : 14
# Rank 5 : 13


# first-value()
# productCode having the max msrp
SELECT productCode From products WHERE msrp=(
SELECT MAX(msrp) FROM products
);

# OR
SELECT productCode FROM products ORDER BY msrp DESC LIMIT 1;

# or
SELECT productCode , FIRST_VALUE(productCode) OVER (ORDER BY msrp DESC) AS highest_msrp
FROM products;



USE Intro_sql;

CREATE TABLE sales
(
sales_employee VARCHAR(50) NOT NULL,
fiscal_year INT NOT NULL,
sale DECIMAL(14,2) NOT NULL,
PRIMARY KEY(sales_employee,fiscal_year)
);


INSERT INTO sales VALUES ('Sathya',2016,100),
                    ('Shiva',2020,250),
                    ('Navya',2013,120),
                    ('Divya',2014,205),
                    ('Sneha',2025,520),
                    ('Priya',2015,650);
                    
SELECT * FROM sales;

# Total sales
SELECT SUM(sale) FROM sales;

# Total sales for each fiscal_year
SELECT SUM(sale),fiscal_year FROM sales GROUP BY fiscal_year;


SELECT fiscal_year,sales_employee,sale , SUM(sale) OVER (PARTITION BY fiscal_year)
AS total_sales FROM sales;



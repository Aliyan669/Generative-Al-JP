-- MySQL is the world’s most popular open source database. 
-- According to DB-Engines, MySQL ranks as the second-most-popular database, behind Oracle Database. 
-- MySQL powers many of the most accessed applications, including Facebook, Twitter, Netflix, Uber, Airbnb, Shopify, and Booking.com.

-- MySQL is a relational database management system
-- MySQL is open-source
-- MySQL is free
-- MySQL was first released in 1995
-- MySQL is developed, distributed, and supported by Oracle Corporation
-- MySQL is named after co-founder Monty Widenius's daughter: My
-- MySQL is ideal for both small and large applications
-- MySQL is very fast, reliable, scalable, and easy to use
-- MySQL is cross-platform
-- Data Looks like Excel Sheet (rows and column) and tables


--  Install mysql server, mysql client (workbench), mysql shell

--  https://www.youtube.com/watch?v=2om3byn2lxs
--  https://www.youtube.com/watch?v=GwHpIl0vqY4

-- Keyword: download mysql community server windows

-- Database file location
-- C:\ProgramData\MySQL\MySQL Server 8\data


--    Database Import in Mysql workbench

-- https://www.youtube.com/watch?v=7Cbm5vPQvNI

-- # import below sample database

-- # sample database 1
-- # https://github.com/mdanish0320/teaching-class/blob/master/JP-BE-PY-batch-1/mysql-class/sample-databases/e-commerce-vehicles/vehicle-store-db.sql

-- # sample database 2
-- # https://github.com/mdanish0320/teaching-class/tree/master/JP-BE-PY-batch-1/mysql-class/sample-databases/e-commerce-movies-rental

-- # Import Database From Mysql Workbench then command run
USE classicmodels;

-- # All Table Data Get 
SELECT * from employees;
SELECT * from classicmodels.employees;

-- # LIMIT
select * from employees LIMIT 5;
select * FROM employees LIMIT 2;

-- # Ascending (ASC) & Descending (DESC)
select * from employees ORDER BY firstName;
select * from employees ORDER BY firstName LIMIT 2;
select * from employees ORDER BY firstName ASC;

select * FROM employees ORDER BY firstName DESC;
select * from employees ORDER BY firstName DESC LIMIT 2;

-- # Selected Column Get
select firstname, lastname from employees;

-- # ALIAS
select firstname AS fname, lastname as lname from employees;

-- # OFFSET
select * from employees LIMIT 5;
select * from employees LIMIT 10 OFFSET 0;
select * from employees LIMIT 10 OFFSET 10;
select * from employees LIMIT 10 OFFSET 20;


select * from products;
SELECT * from products order by productLine ASC limit 2;
SELECT * from products order by productVendor DESC;

select * from employees order by firstName;
select * from employees order by firstName ASC, lastname ASC;

select * from employees order by jobTitle, firstName;

-- # Insert Data
insert into employees values ('1002000', 'Zzzz', 'Abdullah', 'x5800', 'abdullah@classicmodelcars.com', '1', NULL, 'President');

-- # Find Data with the Help of (Where & like)
select * from employees;
select * from employees where firstName = "Abdullah";
select * from employees where email = "abdullah@classicodelcars.com";

select * from employees order by jobtitle;
select * from employees where jobtitle = "President";
select * from employees where jobtitle like "Sale% Manager%";

select * from employees where reportsTo IS NULL;

select * from employees where jobtitle = "Sales Rep";
select * from employees where jobtitle = "Sales Rep" AND reportsTo = "1143";
select * from employees where jobtitle = "Sales Rep" OR reportsTo = "1143";

-- # Update Data
update employees set reportsTo = 1143 where employeeNumber = 1102;

select
*
from
employees 
where 
jobtitle = "Sales Rep" 
    AND reportsTo = "1143" 
	AND officeCode != 1
;

select
*
from
employees
where
jobtitle = "Sales Rep"
    AND reportsTo = "1143"
    AND (officeCode = 2 OR officeCode = 3)
;

select
*
from
employees
where
jobtitle = "Sales Rep"
    AND reportsTo = "1143"
    AND officeCode IN (2, 3)
;

Select * from orders;
select * from orders where orderDate = "2003-01-06";
select * from orders where MONTH(orderDate) = 1;
select * from orders where MONTH(orderDate) = 1 AND YEAR(orderDate) = 2003;

-- # Maximum (MAX) & Minimun (MIN) Sorting 
select * from orderdetails;
select MAX(quantityOrdered) from orderdetails;

select * from payments;
select * from payments where YEAR(paymentDate) = 2003;
select MAX(amount) from payments where YEAR(paymentDate) = 2003;
select MIN(amount) from payments where YEAR(paymentDate) = 2003;

select MAX(amount) from payments;
select MAX(amount) from payments where YEAR(paymentDAte) = 2003;
select MAX(amount) from payments where YEAR(paymentDAte) = 2004;
select MAX(amount) from payments where YEAR(paymentDAte) = 2005;
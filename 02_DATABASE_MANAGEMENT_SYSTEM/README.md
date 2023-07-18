# README

This README file provides information about the database operations performed in the project.

## Table of Contents
- [Show Databases](#show-databases)
- [Create Databases](#create-databases)
- [Use Database](#use-database)
- [Create Tables](#create-tables)
- [Drop Tables](#drop-tables)
- [Insert Table Data](#insert-table-data)
- [Constraint](#constraint)
- [Update](#update)
- [Delete](#delete)
- [Simple Select](#simple-select)
- [Select Operation Advance](#select-operation-advance)
- [Arithmetic Operations](#arithmetic-operations)
- [Comparison Operators](#comparison-operators)
- [Logical Operators](#logical-operators)
- [IN, NOT IN, LIKE, AS Operators](#in-not-in-like-as-operators)
- [Show All Tables in Database](#show-all-tables-in-database)
- [Functions](#functions)
  - [SELECT UPPER](#select-upper)
  - [SELECT LOWER](#select-lower)
  - [SELECT ABS](#select-abs)
  - [SELECT COS](#select-cos)
  - [SELECT ACOS](#select-acos)
  - [SELECT SIN](#select-sin)
  - [SELECT TAN](#select-tan)
  - [SELECT CEIL](#select-ceil)
  - [SELECT FLOOR](#select-floor)
  - [SELECT DEGREES](#select-degrees)
  - [SELECT RADIANS](#select-radians)
  - [SELECT DIV](#select-div)
  - [SELECT EXP](#select-exp)
  - [SELECT GREATEST](#select-greatest)
  - [SELECT LEAST](#select-least)
  - [SELECT LN](#select-ln)
  - [SELECT LOG](#select-log)
  - [SELECT LOG10](#select-log10)
  - [SELECT LOG2](#select-log2)
  - [SELECT MOD](#select-mod)
  - [SELECT PI](#select-pi)
  - [SELECT POW](#select-pow)
  - [SELECT RAND](#select-rand)
  - [SELECT ROUND](#select-round)
  - [SELECT SQRT](#select-sqrt)
  - [SELECT TRUNCATE](#select-truncate)
- [GROUP FUNCTIONS](#group-functions)
  - [MAX](#max)
  - [MIN](#min)
  - [SUM](#sum)
  - [AVG](#avg)
  - [COUNT](#count)
- [GROUP BY FUNCTION](#group-by-function)
- [HAVING](#having)
- [ALTER TABLE](#alter-table)
- [TRUNCATE TABLE](#truncate-table)
- [SUB QUERY](#sub-query)
- [CORRELATED SUBQUERY](#correlated-subquery)
- [JOINING TABLES](#joining-tables)
  - [USING](#using-keyword)
  - [ON](#on-keyword)
  - [SELF JOIN](#self-join)
  - [INNER JOIN](#inner-join)
  - [LEFT JOIN](#left-join)
  - [RIGHT JOIN](#right-join)
  - [FULL JOIN](#full-join)
- [Set Operations](#set-operations)
  - [UNION](#union)
  - [UNION ALL](#union-all)
  - [MINUS](#minus)
- [ON DELETE CASCADE](#on-delete-cascade)
- [Triggers](#triggers)
- [Date and Time Operations](#date-and-time-operations)


## Show Databases

To display the available databases, execute the following command:

```sql
SHOW DATABASES;
```

## Create Databases

To create a new database, execute the following command:

```sql
CREATE DATABASE second_week;
```

## Use Database

To switch to a specific database, use the following command:

```sql
USE DATABASE second_week;
```

## Create Tables

To create a table in the current database, execute the following command:

```sql
CREATE TABLE student(
    Roll INT,
    Name VARCHAR(25),
    Contact_No CHAR(13),
    Email_id VARCHAR(25)
);
```

## Drop Tables

To drop a table from the current database, execute the following command:

```sql
DROP TABLE student;
```

## Insert Table Data

To insert data into the student table, use the following command:

```sql
INSERT INTO student(Roll, Name, Contact_No, Email_id)
VALUES(101, "Hasif", "8801773684304", "h@gmail.com");
```

## Constraint

To create a table with constraints, execute the following command:

```sql
CREATE TABLE student(
    Roll INT NOT NULL UNIQUE PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Contact_No CHAR(13) NOT NULL UNIQUE,
    Email_id VARCHAR(25) NOT NULL UNIQUE,
    Age INT CHECK(Age >= 0)
);
```

## Update

To update records in the student table, use the following command:

```sql
UPDATE student
SET Age = 15
WHERE Roll = 102;
```

## Delete

To delete records from the student table, use the following command:

```sql
DELETE FROM student
WHERE Roll = 103;
```

## Simple Select

To retrieve data from the student table, use the following commands:

```sql
SELECT * FROM student
WHERE Roll = 110;

SELECT Name, Roll FROM student
WHERE Roll = 110;
```

## Select Operation Advance

The following are some advanced select operations:

### DISTINCT

To select distinct values from a column, use the `DISTINCT` keyword. For example:

```sql
SELECT DISTINCT region_id FROM countries;
```

### ORDER BY

To order the result set by one or more columns, use the `ORDER BY` clause. You can specify the sorting order as ASC (ascending) or DESC (descending). For example:

```sql
SELECT *
FROM departments
WHERE ...
ORDER BY location_id ASC;

SELECT *
FROM employees
WHERE department_id = 90
ORDER BY first_name ASC;

SELECT *
FROM departments
ORDER BY location_id DESC;
```

### LIMIT

To limit the number of rows returned by a query, you can use the `LIMIT` clause. It allows you to specify the maximum number of rows to be returned. Additionally, you can use the `OFFSET` clause to skip a certain number of rows before returning the result set. For example:

```sql
SELECT *
FROM employees
LIMIT 10 OFFSET 15;
```

## Arithmetic Operations

You can perform arithmetic operations in SQL queries. Here are some examples:

```sql
SELECT 5 + 3;
SELECT 5 - 3;
SELECT 5 * 3;
SELECT 5 / 3;
SELECT 5 % 3;
```

## Comparison Operators

You can use comparison operators to filter data based on specific conditions. Here are some examples:

```sql
SELECT first_name, salary, email
FROM employees
WHERE salary = 9000;

SELECT first_name, salary, email
FROM employees
WHERE salary != 9000;

SELECT first_name, salary, email
FROM employees
WHERE salary <= 9000;

SELECT first_name, salary, email
FROM employees
WHERE salary >= 9000;

SELECT first_name, salary, email
FROM employees
WHERE salary < 9000;

SELECT first_name, salary, email
FROM employees
WHERE salary > 9000;

SELECT first_name, salary, email
FROM employees
WHERE salary BETWEEN 9000 AND 15000;
```

## Logical Operators

You can use logical operators to combine conditions in SQL queries. Here are some examples:

```sql
SELECT first_name, salary, email
FROM employees
WHERE first_name = "John" AND salary >= 2000;

SELECT first_name, salary, email
FROM employees
WHERE first_name = "John" OR salary >= 2000;
```

## IN, NOT IN, LIKE, AS Operators

You can use the `IN`, `NOT IN`, `LIKE`, and `AS` operators in SQL queries. Here are some examples:

```sql
SELECT *
FROM employees
WHERE job_id IN("AD_PRES", "AD_VP", "FI_MGR");

SELECT *
FROM employees
WHERE job_id NOT IN("AD_PRES", "AD_VP", "FI_MGR");

SELECT *
FROM employees
WHERE first_name LIKE "D%";

SELECT *
FROM employees
WHERE first_name LIKE "%D";

SELECT *
FROM employees
WHERE first_name LIKE "%D%";

SELECT first_name AS NAME
FROM employees;
```

## Show All Tables in Database
```sql
SELECT *
FROM information_schema.tables
WHERE table_type='BASE TABLE'
      AND table_schema = 'hr'
```
## Functions

### SELECT UPPER

Converts a string to uppercase.

Example:
```sql
SELECT UPPER("nihad Hossain");
```

### SELECT LOWER

Converts a string to lowercase.

Example:
```sql
SELECT LOWER("NIHGAD Hossain");
```

### SELECT ABS

Returns the absolute value of a number.

Example:
```sql
SELECT ABS(-2);
```

### SELECT COS

Returns the cosine of an angle.

Example:
```sql
SELECT COS(90);
```

### SELECT ACOS

Returns the inverse cosine (also known as arccosine) of a number.

Example:
```sql
SELECT ACOS(30);
```

### SELECT SIN

Returns the sine of an angle.

Example:
```sql
SELECT SIN(45);
```

### SELECT TAN

Returns the tangent of an angle.

Example:
```sql
SELECT TAN(60);
```

### SELECT CEIL

Returns the smallest integer greater than or equal to a number.

Example:
```sql
SELECT CEIL(45.969);
```

### SELECT FLOOR

Returns the largest integer less than or equal to a number.

Example:
```sql
SELECT FLOOR(45.969);
```

### SELECT DEGREES

Converts an angle from radians to degrees.

Example:
```sql
SELECT DEGREES(45.969);
```

### SELECT RADIANS

Converts an angle from degrees to radians.

Example:
```sql
SELECT RADIANS(45.969);
```

### SELECT DIV

Performs integer division and returns the quotient.

Example:
```sql
SELECT 10 DIV 5;
```

### SELECT EXP

Returns Euler's number raised to the power of a number.

Example:
```sql
SELECT EXP(10);
```

### SELECT GREATEST

Returns the greatest value among a list of values.

Example:
```sql
SELECT GREATEST(1,2,3,4,5);
```

### SELECT LEAST

Returns the least value among a list of values.

Example:
```sql
SELECT LEAST(1,2,3,4,5);
```

### SELECT LN

Returns the natural logarithm of a number.

Example:
```sql
SELECT LN(4.5);
```

### SELECT LOG

Returns the logarithm of a number to the specified base.

Example:
```sql
SELECT LOG(4.5);
```

### SELECT LOG10

Returns the base-10 logarithm of a number.

Example:
```sql
SELECT LOG10(4.5);
```

### SELECT LOG2

Returns the base-2 logarithm of a number.

Example:
```sql
SELECT LOG2(4.5);
```

### SELECT MOD

Returns the remainder of a division operation.

Example:
```sql
SELECT 10 MOD 3;
```

### SELECT PI

Returns the value of pi (π).

Example:
```sql
SELECT PI();
```

### SELECT POW

Returns a number raised to the power of another number.

Example:
```sql
SELECT POW(2,4);
```

### SELECT RAND

Returns a random number.

Example:
```sql
SELECT RAND();
```

### SELECT ROUND

Rounds a number to a specified number of decimal places.

Example:
```sql
SELECT ROUND(45.56565,2);
```

### SELECT SQRT

Returns the square root of a number.

Example:
```sql
SELECT SQRT(100);
```

### SELECT TRUNCATE

Truncates a number to a specified number of decimal places.

Example:
```sql
SELECT TRUNCATE(45.543456,2);
```

## GROUP FUNCTIONS

### MAX

Returns the maximum value in a column.

Example:
```sql
SELECT MAX(salary)
FROM employees;
```

### MIN

Returns the minimum value in a column.

Example:
```sql
SELECT MIN(salary)
FROM employees;
```

### SUM

Returns the sum of values in a column.

Example:
```sql
SELECT SUM(salary)
FROM employees;
```

### AVG

Returns the average value of a column.

Example:
```sql
SELECT AVG(salary)
FROM employees;
```

### COUNT

Returns the number of rows in a table or the number of non-null values in a column.

Example:
```sql
SELECT COUNT(employee_id)
FROM employees;

SELECT COUNT(*)
FROM employees;
```

## GROUP BY FUNCTION

Performs aggregation on a specific column or columns and groups the result by one or more columns.

Example:
```sql
SELECT job_id, COUNT(*)
FROM employees
GROUP BY job_id;
```

## HAVING

Filters the result set based on a condition applied to aggregated data.

Example:
```sql
SELECT COUNT(*), job_id
FROM employees
GROUP BY job_id
HAVING COUNT(*) > 1;
```

## ALTER TABLE

Adds a

 new column to an existing table.

Example:
```sql
ALTER TABLE employees 
ADD doc VARCHAR(5);
```

## TRUNCATE TABLE

Removes all data from a table.

Example:
```sql
TRUNCATE TABLE student;
```

## SUB QUERY

Performs a query inside another query.

Example:
```sql
SELECT first_name, last_name
FROM employees
WHERE salary > (
	SELECT AVG(salary)
    FROM employees
    WHERE first_name = "LEX"
);
```

Example:
```sql
SELECT first_name, last_name
FROM employees
WHERE employee_id != 107 AND salary = (
	SELECT salary
    FROM employees
    WHERE employee_id = 107
);
```

Example:
```sql
SELECT first_name, last_name, job_id
FROM employees
WHERE job_id = (
	SELECT job_id
    FROM employees
    WHERE employee_id = 107
);
```

Example:
```sql
SELECT first_name, last_name, salary, job_id
FROM employees
WHERE job_id = (
	SELECT job_id
    FROM employees
    WHERE employee_id = 107
) AND (salary > (
	SELECT salary
    FROM employees
    WHERE first_name = "Bruce"
));
```

Example:
```sql
SELECT first_name, last_name, salary, job_id
FROM employees
WHERE job_id != 'IT_PROG'
AND salary < ANY (
	SELECT salary
	FROM employees
	WHERE job_id = 'IT_PROG'
);
```

## CORRELATED SUBQUERY

Performs a subquery that refers to a column from the outer query.

Example:
```sql
SELECT *
FROM employees e1
WHERE 3 <= (
	SELECT COUNT(*)
	FROM employees e2
	WHERE e2.salary > e1.salary
);
```

Example:
```sql
SELECT *
FROM employees E1
WHERE NOT EXISTS (
	SELECT *
	FROM employees E2
	WHERE E2.department_id = E1.department_id AND E2.salary > E1.salary
);
```

## JOINING TABLES

Combines rows from two or more tables based on a related column between them.

Example:
```sql
SELECT student.ROLL, student.NAME, result.GPA
FROM student, result
WHERE student.ROLL = result.Roll;
```

Example:
```sql
SELECT e.first_name, e.last_name, e.employee_id, d.department_name, e.department_id
FROM employees e, departments d
WHERE e.department_id = d.department_id;
```

Example:
```sql
SELECT e.first_name, e.last_name, e.employee_id, e.job_id, e.salary, e.department_id, d.department_name
FROM employees e JOIN departments d USING (department_id);
```

Example:
```sql
SELECT e.first_name, e.last_name, e.employee_id, e.job_id, e.salary, e.department_id, d.department_name
FROM employees e JOIN departments d ON (e.department_id = d.department_id);
```

## SELF JOIN

Joins a table with itself.

Example:
```sql
SELECT e.first_name, m.first_name
FROM employees e JOIN employees m ON (e.manager_id = m.employee_id);
```

## INNER JOIN

Returns rows that have matching values in both tables involved in the join.

Example:
```sql
SELECT e.first_name, e.last_name, e.employee_id, j.start_date
FROM employees e INNER JOIN job_history j ON (e.employee_id = j.employee_id);
```

## LEFT JOIN

Returns all rows from the left table and the matching rows from the right table. If there is no match, NULL values are returned for the right table's columns.

Example:
```sql
SELECT e.first_name, e.last_name, e.employee_id, j.start_date
FROM employees e LEFT JOIN job_history j ON (e.employee_id = j.employee_id);
```

## RIGHT JOIN

Returns all rows from the right table and the matching rows from the left table. If there is no match, NULL values are returned for the left table's columns.

Example:
```sql
SELECT e.first_name, e.last_name, e.employee_id, j.start_date
FROM employees e RIGHT JOIN job_history j ON (e.employee_id = j.employee_id);
```

## FULL JOIN

Returns all rows from both tables. If there is no match, NULL values are returned for columns in the non-matching table.

Example:
```sql
SELECT e.first_name, e.last_name, e.employee_id, j.start_date
FROM employees e FULL JOIN job_history j ON (e.employee_id = j.employee_id);
```

## Set Operations

### UNION

Performs a union operation between two result sets.

Example:
```sql
SELECT employee_id
FROM employees
UNION
SELECT job_id
FROM job_history;
```

### UNION ALL

Performs a union operation including duplicate values.

Example:
```sql
SELECT employee_id, first_name
FROM employees
UNION ALL
SELECT job_id, start_date
FROM job_history;
```

### MINUS

Performs a set difference operation between two result sets.

Example:
```sql
SELECT employee_id, first_name
FROM employees
MINUS
SELECT job_id, start_date
FROM job_history;
```

## ON DELETE CASCADE

Applies cascading deletes to maintain referential integrity.

Example:
```sql
USE THIRD_WEEK_PRACTICE;
CREATE TABLE student (
	ID INT PRIMARY KEY,
    NAME VARCHAR(25),
    AGE INT
);
INSERT INTO student (ID, NAME, AGE)
VALUES (101, "A", 15),
       (102, "B", 16),
       (103, "C", 17);

CREATE TABLE course (
	Course_Code INT PRIMARY KEY,
    Course_Name VARCHAR(25)
);

INSERT INTO course (Course_Code, Course_Name)
VALUES (111, "C"),
       (112, "C++"),
       (113, "Algo");

CREATE TABLE enroll (
	ID INT,
    Course_Code INT,
    Journey_Started_date DATE,
    PRIMARY KEY (ID, Course_Code),
    FOREIGN KEY (ID)
		REFERENCES student (ID)
        ON DELETE CASCADE,
	FOREIGN KEY (Course_Code)
		REFERENCES course (Course_Code)
		ON DELETE CASCADE
);

INSERT INTO enroll (ID, Course_Code, Journey_Started_date)
VALUES (101, 112, "2023-07-07"),
       (103, 111, "2023-07-07"),
       (101, 113, "2023-07-07");
```

## Triggers

Triggers are defined actions that are automatically executed in response to specific events.

Example:
```sql
CREATE TRIGGER auto_cap
BEFORE INSERT ON student
FOR EACH ROW
SET NEW.Name = UPPER(NEW.Name);
```

## Date and Time Operations

Performing operations and functions on dates and times.

Example:
```sql
SELECT DAYOFMONTH("2023-07-13");
SELECT MONTH("2023-07-13");
SELECT ADDDATE("2023-07-13", 19);

SELECT ADDTIME("2017-06-15 09:34:21", "05:50:21");
SELECT CONVERT_TZ('2008-05-15 12:00:00', '+00:00', '+10:00');
SELECT CURDATE();
SELECT CURTIME();
SELECT CURTIME(4);
SELECT DATE("2017-06-15 09:34:21");
SELECT DATEDIFF("2017-06-15 09:34:21", "2019-06-05");
SELECT DATE_ADD("2023-07-13", INTERVAL 1 DAY);
SELECT DATE_SUB("2023-07-13", INTERVAL 1 YEAR);

SELECT DATE_FORMAT("2023-07-13", '%W %M %Y');
SELECT DATE_FORMAT("2023-07-13 09:34:21", '%H %i %s');
SELECT DAYOFWEEK("2023-07-13");
```


Feel free to modify and add more details to this README file as per your project requirements.
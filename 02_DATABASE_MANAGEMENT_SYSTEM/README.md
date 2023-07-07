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

Feel free to modify and add more details to this README file as per your project requirements.
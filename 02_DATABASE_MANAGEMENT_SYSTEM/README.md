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

Add description here for advanced select operations.

```sql
-- Advanced select query goes here
```

Feel free to modify and add more details to this README file as per your project requirements.
# Lab Test One Database Documentation

This documentation provides an overview of the database structure, its tables, and the SQL commands used to create, modify, and manipulate the Lab Test One database. The database contains information about students, their library activities, and various details related to them.

## Table of Contents

- [Lab Test One Database Documentation](#lab-test-one-database-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Database Schema](#database-schema)
  - [Table Descriptions](#table-descriptions)
    - [Student](#student)
    - [Library](#library)
    - [Student\_INFO](#student_info)
    - [Student\_data\_set](#student_data_set)
  - [SQL Commands](#sql-commands)
    - [Creating the Database](#creating-the-database)
    - [Creating Tables](#creating-tables)
    - [Renaming Tables](#renaming-tables)
    - [Altering Tables](#altering-tables)
    - [Describing Tables](#describing-tables)
    - [Dropping Tables](#dropping-tables)

## Introduction

The Lab Test One Database is designed to store information about students, their library interactions, and various attributes related to their academic progress. The database is structured using SQL tables and relationships to ensure data integrity and accessibility.

## Database Schema

The Lab Test One Database consists of the following tables:

1. **Student**: Contains information about students' general details and academic information.
2. **Library**: Stores information about books borrowed by students from the library.
3. **Student_INFO**: A duplicate of the "Student" table with the same structure.
4. **Student_data_set**: A modified version of the "Student_INFO" table with additional columns.

## Table Descriptions

### Student

- **Name**: The student's full name (not null).
- **id**: Primary key, auto-incremented student ID.
- **cur_class**: The current class of the student (not null).
- **GPA**: Grade Point Average of the student (not null).
- **is_covid_TEST**: Indicates whether the student has taken a COVID-19 test (default: false).
- **DOB**: Date of Birth of the student.

### Library

- **Book_Name**: The name of the borrowed book (not null).
- **who_hired**: Foreign key referencing the student who borrowed the book.
- **Date_T**: Date when the book was borrowed.
- The "who_hired" field references the "id" column of the "Student" table with cascading delete.

### Student_INFO

(Duplicate of the "Student" table)

### Student_data_set

- The "Student_data_set" table is an altered version of "Student_INFO" with additional columns:
  - **is_passed**: Indicates whether the student has passed (default: false).
  - **AGE**: Age of the student (not null).
  - The "cur_class" column has been dropped and the "is_passed" column has been moved.

## SQL Commands

### Creating the Database

```sql
CREATE DATABASE Lab_Test_One;
USE Lab_Test_One;
```

### Creating Tables

```sql
CREATE TABLE Student (
  Name VARCHAR(35) NOT NULL,
  id INT PRIMARY KEY AUTO_INCREMENT,
  cur_class VARCHAR(20) NOT NULL,
  GPA FLOAT NOT NULL,
  is_covid_TEST BOOLEAN DEFAULT FALSE,
  DOB DATE
);

CREATE TABLE Library (
  Book_Name VARCHAR(25) NOT NULL,
  who_hired INT,
  Date_T DATE,
  FOREIGN KEY (who_hired) REFERENCES Student(id) ON DELETE CASCADE
);

CREATE TABLE Student_INFO AS SELECT * FROM Student;

CREATE TABLE Student_data_set AS SELECT * FROM Student_INFO;
```

### Renaming Tables

```sql
RENAME TABLE Student_DATA TO Student_INFO;
```

### Altering Tables

```sql
ALTER TABLE Student_INFO RENAME TO Student_data_set;

ALTER TABLE Student_data_set ADD is_passed BOOLEAN DEFAULT FALSE;

ALTER TABLE Student_data_set ADD AGE INT NOT NULL AFTER id;

ALTER TABLE Student_data_set MODIFY is_passed VARCHAR(30) AFTER GPA;

ALTER TABLE Student_data_set CHANGE cur_class present_class VARCHAR(20);

ALTER TABLE Student_data_set DROP cur_class;
```

### Describing Tables

```sql
DESCRIBE Student_data_set;
```

### Dropping Tables

```sql
DROP TABLE Student_data_set;
```

Please note that these SQL commands can be executed in a MySQL-compatible database management system. Before executing these commands on your database, ensure that you have a backup of your data, as some of the commands involve altering and dropping tables.
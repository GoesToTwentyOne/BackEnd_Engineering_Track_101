# README.md

This repository contains Python code snippets for working with MySQL databases. The code demonstrates various operations such as creating a database, creating tables, inserting data, querying data, and updating data.

## Table of Contents

- [Setting up the Connection](#setting-up-the-connection)
- [Creating a Database](#creating-a-database)
- [Creating a Table](#creating-a-table)
- [Inserting Data](#inserting-data)
- [Querying Data](#querying-data)
- [Updating Data](#updating-data)

## Setting up the Connection

The following code snippet demonstrates how to establish a connection to a MySQL database:

```python
import mysql.connector

mydb = mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75"
)

print(mydb)
```

## Creating a Database

To create a new database, you can use the following code:

```python
import mysql.connector

mydb = mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75"
)

mycursor = mydb.cursor()
db_name = "python_with_mysql"
mysql_command = "CREATE DATABASE " + db_name
mycursor.execute(mysql_command)

mycursor.execute("SHOW DATABASES")
databases = mycursor.fetchall()

for database in databases:
    print(database)
```

## Creating a Table

To create a table within a database, you can use the following code:

```python
import mysql.connector

mydb = mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql"
)

mycursor = mydb.cursor()
sql_command = """
CREATE TABLE student(
    Name INT PRIMARY KEY,
    Roll INT,
    Class VARCHAR(20)
);
"""
mycursor.execute(sql_command)

show_tables = "SHOW TABLES FROM python_with_mysql"
mycursor.execute(show_tables)
tables = mycursor.fetchall()

for table in tables:
    print(table)
```

## Inserting Data

To insert data into a table, you can use the following code:

```python
import mysql.connector

mydb = mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql"
)

mycursor = mydb.cursor()

sql_command = """
INSERT INTO student(Name,Roll,Class) 
VALUES("A","101","seven"),
    ("B","102","Eight"),
    ("C","103","Nine"),
    ("D","104","Eleven"),
    ("E","105","Twelve");
"""
mycursor.execute(sql_command)
mydb.commit()

mycursor.execute("SELECT * FROM student;")
datas = mycursor.fetchall()

for data in datas:
    print(data)
```

## Querying Data

To retrieve data from a table, you can use the following code:

```python
import mysql.connector

mydb = mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student;")
datas_first = mycursor.fetchall()

for data in datas_first:
    print(data)
```

## Updating Data

To update data in a table, you can use the following code:

```python
import mysql.connector

mydb = mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student;")
data_first = mycursor.fetchall()

for data in data_first:
    print(data)

sql_command = """
SET SQL_SAFE_UPDATES=0;
UPDATE student
SET Class='BAUST'
WHERE Roll=102;
SET SQL_SAFE_UPDATES=1;
"""
mycursor.execute(sql_command)
mydb.commit()

mycursor.execute("SELECT * FROM student;")
data_last = mycursor.fetchall()

for data in data_last:
    print(data)
```

Feel free to explore and modify the code according to your needs.
import mysql.connector

my_db=mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql",
)

my_cursor=my_db.cursor()
sql_command="""
CREATE TABLE student(
    Name INT PRIMARY KEY,
    Roll INT,
    Class VARCHAR(20)
);"""
my_cursor.execute(sql_command)

show_tables="SHOW TABLES FROM python_with_mysql"
my_cursor.execute(show_tables)
tables=my_cursor.fetchall()

for table in tables:
    print(table)
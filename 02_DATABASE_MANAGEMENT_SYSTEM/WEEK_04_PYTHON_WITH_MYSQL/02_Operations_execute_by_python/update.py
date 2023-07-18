import mysql.connector

my_db = mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql",
)

my_cursor = my_db.cursor()
my_cursor.execute("SELECT * FROM student;")
data_first = my_cursor.fetchall()

for data in data_first:
    print(data)

sql_command = """
SET SQL_SAFE_UPDATES=0;
UPDATE student
SET Class='BAUST'
WHERE Roll=102;
SET SQL_SAFE_UPDATES=1;
"""
my_cursor.execute(sql_command)
my_db.commit()

my_cursor.execute("SELECT * FROM student;")
data_last = my_cursor.fetchall()

for data in data_last:
    print(data)

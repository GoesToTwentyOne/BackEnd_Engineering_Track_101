import mysql.connector
my_db=mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql",
)

my_cursor=my_db.cursor()
my_cursor.execute("SELECT * FROM student;")
datas_first=my_cursor.fetchall()

for data in datas_first:
    print(data)
import mysql.connector

my_db=mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
    database="python_with_mysql",
)

my_cursor=my_db.cursor()

sql_command="""
INSERT INTO student(Name,Roll,Class) 
VALUES("A","101","seven"),
    ("B","102","Eight"),
    ("C","103","Nine"),
    ("D","104","Eleven"),
    ("E","105","Twelve");
"""
my_cursor.execute(sql_command)
my_db.commit()

my_cursor.execute("SELECT * FROM student;")
datas=my_cursor.fetchall()


for data in datas:
    print(data)
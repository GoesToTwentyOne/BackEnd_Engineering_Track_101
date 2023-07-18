import mysql.connector
mydb=mysql.connector.connect(
    user="nihadgo75",
    host="localhost",
    passwd="nihadgo75",
)

mycursor=mydb.cursor()
db_name="python_with_mysql"
mysql_command="CREATE DATABASE "+db_name
mycursor.execute(mysql_command)

mycursor.execute("SHOW DATABASES")
databases = mycursor.fetchall()

for database in databases:
    print(database)
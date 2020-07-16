import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password@123",
auth_plugin='mysql_native_password',
    database='luminar'
)

cursor = db.cursor()

cursor.execute("drop table if exists employee")

sql="""create table employee 
        (first_name varchar(20),
        last_name varchar(20),
        age int(10),
        sex varchar(20),
        income int(20))"""
cursor.execute(sql)
db.close()
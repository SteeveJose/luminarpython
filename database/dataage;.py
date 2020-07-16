import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password@123",
auth_plugin='mysql_native_password',
    database='luminar'
)

cursor = db.cursor()

sql="""select first_name from employee where age>25"""
try:
    cursor.execute(sql)

    data = cursor.fetchall()
    print(data)
except Exception as e:
    print(e.args)
finally:
    db.close()
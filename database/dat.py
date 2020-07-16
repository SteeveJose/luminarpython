import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password@123",
auth_plugin='mysql_native_password'
)

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("database version:",data)

db.close()
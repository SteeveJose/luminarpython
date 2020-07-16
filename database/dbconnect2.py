import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password@123",
auth_plugin='mysql_native_password',
    database='luminar'
)

cursor = db.cursor()

sql="""insert into employee(first_name,last_name,age,sex,income) values ('milda','rieves',30,'F','60000')"""
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
db.close()
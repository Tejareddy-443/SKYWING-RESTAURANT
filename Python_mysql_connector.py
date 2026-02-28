import mysql.connector as conn
connection=conn.connect(host="localhost",user="root",password="Tejareddy1341",database="registered_users")
cursor=connection.cursor()
cursor.execute("insert into users values('1','Tejareddy','teja@1234','1234567890')")
cursor.execute("select * from users")
data=cursor.fetchall()
for i in data:
    print(i)
#connection.commit()
connection.close()
print("Connection successful")
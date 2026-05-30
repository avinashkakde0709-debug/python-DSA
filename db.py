import mysql.connector
try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydb",
    )
    if conn.is_connected():
        print("Connectiion successful!")

except mysql.connector.Error as err:
    print("Error:",err)

cursor=conn.cursor()
cursor.execute("select * from user")
rows=cursor.fetchall()
for r in rows:
    print(r)

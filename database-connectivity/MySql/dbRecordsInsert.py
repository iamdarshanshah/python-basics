import mysql.connector  # Install mysql connector externally using pip3

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='test1234')

if conn.is_connected():
    print("Connected to MySql DB")

cursor = conn.cursor()

try:
    cursor.execute("insert into emp values(1,'John', 200000)")
    conn.commit()
    print('Record inserted')
except:
    conn.rollback()

cursor.close()
conn.close()

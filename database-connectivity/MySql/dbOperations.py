import mysql.connector  # Install mysql connector externally using pip3

# Establish connection
conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='test1234')

if conn.is_connected():
    print("Connected to MySql DB")

# Create cursor object from connection
cursor = conn.cursor()

cursor.execute("Select * from emp")

# Fetch records one by one
row = cursor.fetchone()  # Fetch one record

while row is not None:  # Looping through cursor to fetch all records
    print(row)
    row = cursor.fetchone()


# To fetch all records in one go
rows = cursor.fetchall()
print("total no. of records in db :: {}".format(cursor.rowcount))
for row in rows:
    print(row)


cursor.close()
conn.close()

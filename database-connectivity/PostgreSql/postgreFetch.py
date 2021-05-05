import psycopg2

conn = psycopg2.connect(database="empdb", user="root", password="test1234", host="127.0.0.1", port="5432")

print("connected to emp db")

cursor = conn.cursor()

cursor.execute("select * from employee")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

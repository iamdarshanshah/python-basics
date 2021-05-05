import mysql.connector  # Install mysql connector externally using pip3


def deleteRecordByID(id):
    conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='test1234')
    if conn.is_connected():
        print("connected to db")
        cursor = conn.cursor()
        sqlQuery = 'delete from emp where id = "%d"'
        args = (id)
        try:
            cursor.execute(sqlQuery % args)
            conn.commit()
            print("Record deleted successfully")
        except:
            print("SQL command failed..roll back")
            conn.rollback()
        finally:
            cursor.close()
    else:
        print("Connection failed")
    conn.close()


empId = int(input('Enter EMP ID :: '))
deleteRecordByID(empId)

# Should prompt a user to enter Student's Name, Id and marks and display those details.

studentName = input("Enter Name of student :: ")
studentId = int(input("Enter ID :: "))
studentMarks = float(input("Enter marks :: "))

print("Name : {}, ID : {}, Marks : {}".format(studentName, studentId, studentMarks))
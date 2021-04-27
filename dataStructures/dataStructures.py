student = {'Darshan': ['Python', 'Java'], 'Ravi': ['AWS', 'Java'], 'Kishan': ['Python', 'Spring']}

keys = student.keys()

for eachStudent in keys:
    print('Courses taken by ', eachStudent,'are :')
    for eachCourse in student[eachStudent]:
        print(eachCourse)

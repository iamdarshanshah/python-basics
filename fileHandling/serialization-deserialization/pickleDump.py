import pickle, serialize

f = open("student.dat", "wb")

s = serialize.Student(123, "Darshan", 90.0)

pickle.dump(s, f)

f.close()
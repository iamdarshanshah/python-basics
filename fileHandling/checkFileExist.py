import os, sys

if os.path.isfile('myfile1.txt'):
    f = open('myfile.txt1', 'r')
else:
    print("file doesn't exist")
    sys.exit()

s = f.read()
print(s)
f.close()
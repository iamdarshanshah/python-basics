# Write string to a file #

f = open('myfile.txt', 'w')

s = input("Enter text :: ")

f.write(s)

f.close()

# Read from a file #

f = open("myfile.txt", "r")

s = f.read()

print(s)

f.close()
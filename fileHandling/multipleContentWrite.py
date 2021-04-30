# Writing multiple lines to a file

f = open('myfile.txt', 'w')

print('Enter text. (Type # to end)')

s = ''

while (s != '#'):
    s = input()
    f.write(s)

f.close()

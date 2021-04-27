dic1 = {"name": "John", 2: "bob", True: "bill", "name": 'Darshan'}

print(dic1)

key = dic1.keys()

values = dic1.values()

for i in key: print(i)

for i in values: print(i)

del dic1[2]
print(dic1)
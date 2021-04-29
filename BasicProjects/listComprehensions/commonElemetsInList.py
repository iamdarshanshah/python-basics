# Find common elements in two lists

a = [2, 4, 8, 10, 12]
b = [1, 2, 3, 4, 5]

z = [i for i in a if i in b]

print(z)  # [2, 4]

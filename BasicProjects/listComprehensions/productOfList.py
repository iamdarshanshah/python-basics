# Product of tow list items

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

z = [a[i]*b[i] for i in range(len(a))]

print(z) # [6, 14, 24, 36, 50]

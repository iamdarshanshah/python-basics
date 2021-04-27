import sys

lst = sys.argv

for i in lst: print(i)

print(len(lst))  # 1 as by default program locations is passed

# Product of command line arguments

product = 1
count = 1
for i in sys.argv:
    if count == 1:
        continue
    # assert int(i), "Command line arg not parsable to int"
    product *= int(i)
    count += 1

print(product)

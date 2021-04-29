# Filter even numbers from a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenLst = list(filter(lambda x: x % 2 == 0, lst))

print(evenLst)  # [2, 4, 6, 8, 10]

# Map function to square elements of list
squaredLst = list(map(lambda x: x ** 2, lst))

print(squaredLst)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Reduce function to sum all elements in a list (Need to import from functools package)
from functools import reduce

sumOfLst = reduce(lambda x, y: x + y, lst)

print(sumOfLst)  # 55

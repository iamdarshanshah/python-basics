from numpy import *

a1 = array([10, 30, 50, 70, 90, 110])
a2 = array([20, 40, 60, 80, 100, 102])

print(a1 > a2)  # [False False False False False True]

print(a1 < a2)  # [ True  True  True  True  True False]

print(any(a1 > a2))  # True

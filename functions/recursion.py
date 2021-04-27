# Calculate factorial of number using recursion
"""
E.g. :- factorial(3)
- factorial(3) = 3 X factorial(2)
- factorial(2) = 2 X factorial(1)
- factorial(1) = 1 X factorial(0)
- factorial(0) = 1
"""

"""
How to write recursive functions
- Define an end condition
- else call the function again

Note :- to be used when repeating logic is to be used for calculation
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(7))

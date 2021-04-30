# Throw and handle ZeroDivisionError
a, b = [int(x) for x in input("Enter two numbers :: ").split(',')]
print(a, b)

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Exception did not occur")
finally:
    print("Code needs to be executed")

# Display numbers 1...20 using while
x = 1
while x <= 20:
    print(x)
    x += 1

print("Final x :: {}".format(x))

# Display odd numbers between given numbers
# x = int(input("Enter min number :: "))
# y = int(input("Enter max number :: "))
x, y = 20, 30
while x <= y:
    if x % 2 != 0:
        print(x)
    x += 1

# For loop - display numbers from 50 to 70 step 2
for i in range(50, 71, 2):
    print(i)


# Using Assert in program
x = int(input("Enter number greater than 10 :: "))
assert x>10, "X is less than 10"
print("You entered {}".format(x))
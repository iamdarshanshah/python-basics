# Fisrt basic function
def avg(a, b):
    print("average of {} and {} = {}".format(a, b, (a + b) / 2))


avg(16, 35)


# Returning a value from function
def avg(a, b):
    return (a + b) / 2


average = avg(10, 30)
print(average)


# Return multiple values (will be returned as tuple)
def calc(a, b):
    w = a * b
    x = a + b
    y = a - b
    z = a / b
    return w, x, y, z


calculations = calc(10, 5)
for i in calculations: print(i)

# Assigning function to a variable
x = 123


def display():
    x = 678
    print(x)
    print(globals()['x'])


z = display
z();
z();  # same as display()
display();  # same as z()


# Inner Functions (function inside function)

def greet(name):
    def message():
        return "Hello "

    greetings = message() + name
    return greetings


print(greet("Darshan"))  # Hello Darshan


# print(message()) -> variable message not accessible outside


# Function as a parameter to other function
def greet(func):
    return "Hello " + func


def name(a):
    return a


print(greet(name("Darshan")))  # Hello Darshan


# Returning function from function
def greet():
    def message():
        return "Hello"
    return message


fun = greet()
print(fun())  # Hello

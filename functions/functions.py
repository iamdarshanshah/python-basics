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

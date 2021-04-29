# Creating a custome generator function

def customGenerator(x, y):
    while (x < y):
        yield x
        x += 1


result = customGenerator(2, 10)
for i in result: print(i)

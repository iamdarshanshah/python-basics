import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)

try:
    f = open("myfile.txt", 'w')
    a, b = [int(x) for x in input("Enter two number space separated :: ").split()]
    logging.info("Performing division write to file")
    f.write("Writing to file {}::".format(a / b))
except ZeroDivisionError:
    print("Division by zero not allowed")
    logging.error("Division by zero")
else:
    print("Write to file successful")
finally:
    f.close()
    print("file closed")
print("code after exception")

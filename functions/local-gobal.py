## Accessing gobal variable in python function

gloabl_var = 2021

def printVariable():
    local_var = 2020
    print(gloabl_var) #2021
    print(local_var) #2020

printVariable()

# Gloabal and local variable has same name (Local variable will take precedence

var = 2021

def printVar():
    var = 2020
    print(var) #2020

printVar()
print(var) #2021

# Accessing global and local variable with same name in function (using globals() function)

a = 2021

def printYear():
    a=2020
    print("Last year :: {}".format(a)) #2020
    print("Current year :: {}".format(globals()['a'])) #2021

printYear()
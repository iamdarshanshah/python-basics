# Pass n number of optional parameters (using *) to function and x number of keyword parameters (using **) to a function

def printArgs(x, *args, **kwargs):  # x is mandatory, *args = tuple of n number of parameters, **kwargs = dictionary of keyword parameters
    print(x)
    print(args)
    print(kwargs)


printArgs(10)
"""
output :
10
()
{}
"""

printArgs(10, 20, "Darshan", True)
"""
output :
10
(20, 'Darshan', True)
{}
"""

printArgs(10, name="Darshan", isMale=True)
"""
output :
10
()
{'name': 'Darshan', 'isMale': True}
"""

printArgs(10, 20, 30, name="Darshan", isMale=True)
"""
output :
10
(20, 30)
{'name': 'Darshan', 'isMale': True}
"""

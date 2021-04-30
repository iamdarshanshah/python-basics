"""Define a class Patient
    with 3 private fields which can be accessed only through setter and getter methods
    Initialize them using constructor
"""


class Patient:
    def __init__(self):
        self.__name = "John"
        self.__age = 20
        self.__id = 11

    def setName(self, n):
        self.__name = n

    def getName(self):
        return self.__name

    def setAge(self, n):
        self.__age = n

    def getAge(self):
        return self.__age

    def setId(self, n):
        self.__id = n

    def getId(self):
        return self.__id


p = Patient()
p.setId(10)
p.setAge(22)
p.setName("Darshan")

print(p.getName(), p.getAge(), p.getId())

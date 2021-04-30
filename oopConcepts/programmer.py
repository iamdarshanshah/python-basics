class Programmer:
    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self, techs):
        self.technologies = techs

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()
p1.setName("Darshan")
p1.setSalary(10000)
p1.setTechnologies(['Java', 'Hibernate', 'Python'])

print(p1.getName(), p1.getSalary(), p1.getTechnologies())

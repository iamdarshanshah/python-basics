# Capture patient information and its clinical data information

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []  # Has A Relationship

    def addClinicalData(self, clinical):
        self.clinical.append(clinical)


class Clinical:
    def __init__(self, componentName, componentValue):
        self.componentName = componentName
        self.componentValue = componentValue


p = Patient("Dars", 22)
c1 = Clinical("BP", "80/100")
c2 = Clinical("HeartRate", "80PM")

p.addClinicalData(c1)
p.addClinicalData(c2)

print(p.name)

for eachClinical in p.clinical:
    print(eachClinical.componentName)
    print(eachClinical.componentValue)
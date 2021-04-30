class Product:
    objectCunt = 0
    def __init__(self):  # Constructor
        self.name='iPhone'
        self.description='It is Iphone'
        self.price=700.0
        Product.objectCunt+=1

    @staticmethod
    def displayCount():
        print(Product.objectCunt)


p1 = Product()

print(p1.price)
print(p1.description)
print(p1.name)

p2 = Product()

print(p2.price)
print(p2.description)
print(p2.name)

Product.displayCount()
## Using a boolean flag

from threading import *
from time import *

class Producer:
    def __init__(self):
        self.productList = []
        self.ordersPlaced = False

    def produce(self):
        for i in range(1,5):
            self.productList.append("Product"+str(i))
            sleep(1)
            print("Product Added")
        self.ordersPlaced = True

class Consumer:
    def __init__(self, producerThread):
        self.prod = producerThread

    def consume(self):
        while self.prod.ordersPlaced == False:
            sleep(0.2)
        print("Orders processed :: ", self.prod.productList)


p = Producer()
c = Consumer(p)


t1 = Thread(target=p.produce)

t2 = Thread(target=c.consume)

t1.start()
t2.start()


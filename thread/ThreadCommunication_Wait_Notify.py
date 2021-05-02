# Wait and notify should be used in a synchronized context

from threading import *
from time import *

class Producer:
    def __init__(self):
        self.productList = []
        self.c = Condition()  # Create condition object

    def produce(self):
        self.c.acquire()  # Acquire lock
        for i in range(1,5):
            self.productList.append("Product"+str(i))
            sleep(1)
            print("Product Added")
        self.c.notify()  # Notifying consumer
        self.c.release()  #  Releasing lock

class Consumer:
    def __init__(self, producerThread):
        self.prod = producerThread

    def consume(self):
        self.prod.c.acquire()  # acquiring lock
        self.prod.c.wait(timeout=0)  # Waiting for producer to finish
        print("Orders processed :: ", self.prod.productList)
        self.prod.c.release()  # Release the lock


p = Producer()
c = Consumer(p)


t1 = Thread(target=p.produce)

t2 = Thread(target=c.consume)

t1.start()
t2.start()


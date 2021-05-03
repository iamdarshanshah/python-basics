# Not desirable to corrupt resources being used by other thread
"""
Achieved using thread lock
- semaphores
- locks
"""

# Using Locks/Semaphore

from threading import *
from time import sleep


class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Lock()  # self.l = Semaphore()

    def buy(self, seatsRequest):
        self.l.acquire()
        sleep(3)
        if seatsRequest <= self.availableSeats:
            print("Processing payment")
            print("Seat Confirmed")
            print("Printing ticket")
            self.availableSeats -= seatsRequest
        else:
            print("Sorry resquested no. of seats not available")
        self.l.release()


obj = BookMyBus(10)

t1 = Thread(target=obj.buy, args=(3,))

t2 = Thread(target=obj.buy, args=(4,))

t3 = Thread(target=obj.buy, args=(4,))

t1.start()
t2.start()
t3.start()

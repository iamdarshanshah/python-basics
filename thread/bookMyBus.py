from threading import *

class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats

    def buy(self, seatsRequest):
        if(seatsRequest <= self.availableSeats):
            print("Processing payment")
            print("Seat Confirmed")
            print("Printing ticket")
            self.availableSeats-=seatsRequest
        else:
            print("Sorry resquested no. of seats not available")


obj = BookMyBus(10)

t1 = Thread(target=obj.buy, args=(3,))

t2 = Thread(target=obj.buy, args=(4,))

t3 = Thread(target=obj.buy, args=(4,))

t1.start()
t2.start()
t3.start()
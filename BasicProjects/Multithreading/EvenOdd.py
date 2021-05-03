from threading import *


class Even(Thread):
    def run(self):
        i = 1
        while i <= 100:
            if i % 2 == 0:
                print(i)
            i += 1


class Odd:
    def displayOdd(self):
        i = 1
        while i <= 100:
            if i % 2 != 0:
                print(i)
            i += 1


odd = Odd()

t1 = Thread(target=odd.displayOdd)
t2 = Even()

t1.start()
t2.start()

i = 1
while i <= 100:
    print(i)
    i += 1

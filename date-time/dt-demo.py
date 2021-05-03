import time

epochtime = time.time()

print("epoch time {}".format(epochtime))  # Seconds from begining of epoch time

t = time.ctime(epochtime)

print(t)  # Sun May  2 12:48:47 2021

"""
Finding current date and time
"""

import datetime

dt = datetime.datetime.today()

print(dt)  # 2021-05-02 12:50:21.987411
print(dt.day, dt.month, dt.year)  # 2 5 2021
print(dt.hour, dt.minute, dt.second)  # 12 51 38

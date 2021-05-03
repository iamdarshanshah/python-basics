import time
from datetime import date

starttime = time.perf_counter()

ldates = []

d1 = date(2021,5,2)
d2 = date(2018,5,2)
d3 = date(2020,5,2)
d4 = date(2024,5,2)
d5 = date(2019,5,2)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.append(d5)

print(ldates)

ldates.sort()

time.sleep(3)  # sleep program for 3 seconds

print(ldates[0])

endtime = time.perf_counter()

print("Execution time :: {}".format(endtime-starttime))  # Execution time :: 3.0002371

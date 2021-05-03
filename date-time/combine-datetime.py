from datetime import *

d = date(2018,7,21)
t = time(12,53)

dt = datetime.combine(d, t)

print(dt)  # 2018-07-21 12:53:00

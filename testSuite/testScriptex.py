import time
from datetime import datetime

dt = datetime.fromtimestamp(time.time())
date = '빌드날짜 : ' + str(dt)[:16]

print(date)
a = 1
b = 1
for data in range(5):
    c = a + b
    print(c)
time.sleep(67)
et = datetime.fromtimestamp(time.time())

lapse = et - dt
print(lapse)
print('소요시간: ' + str(lapse)[2:4])
import time
from datetime import datetime

dt = datetime.fromtimestamp(time.time())
date = '빌드날짜 : ' + str(dt)[:10]

print(date)
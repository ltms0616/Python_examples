import sys
import random
import time
import datetime
import collections

print(time.gmtime())
print(time.localtime())
fp = open("data.txt", "w")
count=0
random.seed(time.time())
d= datetime.datetime.now()
numbers = range(1,49)
while (datetime.datetime.now()-d).total_seconds()<10:
    fp.write("{:02} {:02} {:02} {:02} {:02} {:02}\n".format(*(random.sample(numbers, 6))))
    time.sleep(1)
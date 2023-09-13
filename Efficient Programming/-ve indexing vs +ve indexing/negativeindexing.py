ls = [i for i in range(1,100)]
import time
start = time.time()
for i in range(1,100000):
    ls[-1]
end = time.time()
print(end-start)
'''
$ python3 time_postiveindexing.py
0.009263992309570312
$ python3 time_negativeindexing.py
0.004432201385498047
'''

import time
start = time.time()
for i in range(1,10000):
    fact = 1
    for i in range(1,11):
        fact *= i
end = time.time()
print(end - start)

'''
$ python3 6while.py
0.010560989379882812
$ python3 6invertedwhile.py
0.00934600830078125
$ python3 6for.py
0.007540464401245117
'''
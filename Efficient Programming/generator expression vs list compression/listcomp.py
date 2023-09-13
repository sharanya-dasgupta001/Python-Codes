import time
from sys import getsizeof
start = time.time()
for i in range(10000):
    lc = [num for num in range(10000)]
    sum(lc)
end = time.time()
print(end - start)
print(getsizeof(lc))

# List Compression taking lesser time than generator exp
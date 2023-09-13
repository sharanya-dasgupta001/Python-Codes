import time
from sys import getsizeof
start = time.time()
for i in range(10000):
    ge = (num for num in range(10000))
    sum(ge)
end = time.time()
print(end - start)
print(getsizeof(ge))

# List Compression taking lesser time than generator exp
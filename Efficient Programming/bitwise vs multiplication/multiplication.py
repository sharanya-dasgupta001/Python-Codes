import time
start = time.time()
m = 123456789
for i in range(1,1000000):
    val = m * 65
end = time.time()
print(end-start)
import time
start = time.time()
x = 0
for i in range(1,100000000):
    -~x
end = time.time()
print(end - start)

# Almost same time
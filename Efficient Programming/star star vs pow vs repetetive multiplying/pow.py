import time
start = time.time()
for i in range(1,1000000):
    m = pow(2,4)
end = time.time()
print(end - start)

# Avoid the use of pow() for computing small integer powers, ** faster, num*num*.. more faster
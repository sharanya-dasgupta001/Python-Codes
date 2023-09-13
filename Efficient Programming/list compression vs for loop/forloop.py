import time
start = time.time()
ls = ['x', 'xyxy', 'xyxyx']
lsNew = []
for l in ls:
    if l == l[::-1]:
        lsNew.append(l)
print(lsNew)
end = time.time()
print(end - start)
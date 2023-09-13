import time
start = time.time()
ls = ['x', 'xyxy', 'xyxyx']
print([l for l in ls if l == l[::-1]])
end = time.time()
print(end - start)
    
# List Comprehension is slower than using for loop, no advantage
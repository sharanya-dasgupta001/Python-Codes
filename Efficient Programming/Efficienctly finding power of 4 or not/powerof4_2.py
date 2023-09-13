'''
Write a program to verify whether a given number is a power
of 4 or not in the best possible way.
'''

import time
n=int(input("Enter the number"))
start = time.time()
if (n&(n-1)) or (n%3!=1):
    print("Not Power of 4")
else:
    print("Power of 4")
end = time.time()
print(end-start)

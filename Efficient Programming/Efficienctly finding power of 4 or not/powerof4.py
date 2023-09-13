'''
Write a program to verify whether a given number is a power
of 4 or not in the best possible way.
'''

import time
n=int(input("Enter the number"))
start=time.time()
while n and (n%4==0):
    n/=4
if n==1:
    print("Power of 4")
else:
    print("Not Power of 4")
end=time.time()
print(end-start)
'''
Write a program to find out the summation of the following
series given n as the user input.
1
-
1
+
11
--
12
+
111
---
123
+ · · · +
111 . . . n times
------------------
123 . . . n
'''
import math
n=int(input())
sum=0
ls=[]
for i in range(n):
    sum += ( 10**i + 1 ) / (10**i + i + 1)
    ls.append( ( 10**i + 1 ) / (10**i + i + 1) )
#print(sum)   
print(math.fsum(ls))
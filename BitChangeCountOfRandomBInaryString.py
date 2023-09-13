'''
Write a program that will print ‘0’ with a probability of 0.5
and ‘1’ in rest of the cases. Now write a function RUN to
count the number of runs in the binary stream generated with
your program. The number of runs will simply explore and
count dichotomous (reflecting contrast between two things)
sequence of values.
Note: The following sequence of 0’s and 1’s has a run count
of nine.
0 0 1 1 0 1 0 0 0 0 1 0 0 1 1 1 1 1 0 0

'''
import random
def run(st):
    runcount=0
    for i in range(len(st)):
        if i==0:
            continue
        else:
            if st[i] != st[i-1]:
                runcount+=1
    return runcount
    
st=""
n=int(input())
for i in range(n):
    st=st+str(random.randint(0, 1))
print(st)
print(run(st))
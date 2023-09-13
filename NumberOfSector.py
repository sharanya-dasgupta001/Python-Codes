'''
Suppose a caterer needs to cut a circular pankake into
maximum number of pieces (not necessarily of the same shape
or size) with a given number of straight cuts. For example, 3
straight cuts across a pancake will produce 6 pieces if the cuts
are made intersecting at a common point, but 7 if they do not.
Write a program to print the maximum number of pieces that
can be obtained with a given number of straight cuts as input.
'''
n=int(input("Enter number of straight cuts:"))
n1=2
if n==1 :
    print(n1)
else:
    for i in range(n-1):
        n1+=i+2
    print(n1)

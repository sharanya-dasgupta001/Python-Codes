'''
Given a positive integer n as user input, find out the number
of trailing zeros in n!.
Note: This can be done with log5 n number of divisions
'''
def TrailZero(n):
    count = 0
    while n:
        n //= 5
        count += n
    return count
n = input("Enter n: ")
print(n + '! has', TrailZero(int(n)), 'trailing zeros')
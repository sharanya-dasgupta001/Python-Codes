'''
Write a program to print the following pattern using generic
controls over print. Let the line number be user input.
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
'''
n=input("Enter the number")
n=int(n)
for i in range(0,(n//2)):
	for k in range(0,i):
		print(" ", end="")
	print("*", end="")
	for j in range(i+1,n-i-1):
		print(" ", end="")
	print("*")
if n%2 != 0 :
	for i in range(0,(n//2)):
		print(" ", end="")	
	print("*")
	
	
for i in range((n//2),0,-1):
	for k in range(i,1,-1):
		print(" ", end="")
	print("*", end="")
	for j in range(n-i,i,-1):
		print(" ", end="")
	print("*")
    



'''
Suppose a list of strings are given as user input. Write a
program to verify whether the ordering of distinct characters
in the last string preserves the ordering of characters in all the
preceding strings. Note that, conflicts of ordering might exist
in the preceding strings.
Note: The inputs apple, apollo, apl preserves the
ordering but not the inputs capacity, pacific, cap.

'''
ls=input("Enter the list of Strings:").split()
flag=0
ref=ls[-1]
for ch in ls[:-1]:
    i,j = 0,0
    while i<len(ref) and j<len(ch):
        if ref[i]==ch[j]:
            i+=1
        j+=1
    if i != len(ref):
        flag=1

if flag == 1:
    print("Not Preserved") 
else:
    print("Preserved")
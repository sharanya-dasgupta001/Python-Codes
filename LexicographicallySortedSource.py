'''
You have to write a program that reads its own source file
(i.e., mtc23xx-day4-prog2.py), and prints the lines in that file
in lexicographically sorted order.

'''

def read(file):
    f=open(file,'r')
    output=f.read()
    f.close()
    return output
output=read('readsource.py')
ls=[]
for i in output:
    #print(i,end='')
    #ls.append(i)
    if (i == '\n'):
        ls.sort()
        for j in ls:
            print(j,end='')
        print('\n')
        ls=[]
    else:
        ls.append(i)
        #print(ls)
ls.sort()
for j in ls:
    print(j,end='')
#print(ls)
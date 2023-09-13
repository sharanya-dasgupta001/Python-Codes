'''
Write a program to reverse the contents of another input file.
'''

def read(file):
    f = open(file, 'r')
    output = f.read()
    f.close()
    return output
output = read('text.txt')
OutputFile = open('result.txt', 'w')
for i in range(len(output)-1,-1,-1):
    print(output[i],end="", file = OutputFile)
OutputFile.close()

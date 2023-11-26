str = "abaaaba"
max='a'
index = []
for i in range(len(str)):
    if str[i]>=max:
        max = str[i]
        index.append(i)
maxsubs=""
for i in index:
    if str[i:len(str)]>=maxsubs:
        maxsubs = str[i:]
print(maxsubs)

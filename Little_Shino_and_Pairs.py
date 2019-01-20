N = int(input())
data = list(map(int, input().split()))
data.sort()
idata = []
jdata = []
flag = 0
for i in data:
    for j in data:
        if i != j and i > j:
            if i not in idata and j not in jdata:
                flag += 1
                idata.append(i)
                jdata.append(j)
print(flag)
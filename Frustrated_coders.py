N=int(input())
coders = list(map(int, input().split()))
coders.sort()
maxdata=max(coders)
indexdata = []
j = 0
i=0
while len(coders) > 0:
    if coders[j] != coders[i] and i not in indexdata:
        coders.pop(j)
        p = i-1
        indexdata.append(p)
        j = 0
        i-=1
    else:
        i+=1
    if coders[i] == maxdata:
        coders.pop(j)
        break
print(sum(coders))

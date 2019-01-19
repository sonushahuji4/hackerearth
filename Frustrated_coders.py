N = int(input())
coders = list(map(int, input().split()))
coders.sort()
indexdata = []
l = [int(x) for x in coders]

for i in range(0, N - 1):
    for j in range(i, N):
        if coders[i] != coders[j] and (j) not in indexdata:
            l[i] = 0
            indexdata.append(j)
            break
print(sum(l))
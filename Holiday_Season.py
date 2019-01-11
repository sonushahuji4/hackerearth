N=int(input())
l=list(map(str,input().split()))
count=0
for a in range(0,N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            for d in range(c+1,N):
                if l[a]==l[c] and l[b]==l[d]:
                    count+=1
print(count)
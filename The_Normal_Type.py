n=int(input())
data=list(map(int,input().split()))
s=len(data)
flag=0
l=[]
for i in range(0,s):
    for j in range(0,s):
        for x in range(i,j+1):
            storedata = data[i]+data[j+1]
            print(storedata)
            l.append(storedata)

print(l)


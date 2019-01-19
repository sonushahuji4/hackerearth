n=int(input())
s=list(map(int,input().split()))
k=[]
i=0
j=i
s=sorted(s,reverse=True)
while(i!=n and j!=n):
    if(s[i]>s[j]):
        k.append(s[j])
        i+=1
        j+=1
    else:
        j+=1
print(sum(s)-sum(k))
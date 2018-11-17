t=int(input())
n,k=map(int,input().split())
data=[]
flag=0
thief=0
while t>0:
    for i in range(0,n):
        l=list(map(str,input().split()))
        s=0
        for j in l:
            if j=='P':
                ckp=s
                if l[ckp+k] == 'T':
                    thief+=1
                    break
            elif j=='T':
                ckp=s
                if l[ckp+k] == 'P':
                    thief += 1
                    break
            s=s+1
    t-=1
print(thief)

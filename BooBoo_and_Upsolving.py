def pzbl(arr,mid,k):
    cnt=1
    s=0
    for i in arr:
        s+=i 
        if s>mid:
            cnt+=1
            s=i
    return cnt<=k
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
low=max(l)
high=sum(l)
ans=1000
while low<=high:
    mid=(low+high)>>1
    if pzbl(l,mid,k):
        high=mid-1
    else:
        low=mid+1
print(low)

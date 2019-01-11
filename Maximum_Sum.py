#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/

n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
count=0
flag=0
if data[0]<0:
    flag=max(data)
    count=1
else:
    for i in data:
        if i>=0:
            flag=flag+i
            count+=1
print(flag,count)

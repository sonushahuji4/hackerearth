#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/min-max-8/
n=int(input())
data=list(map(int,input().split()))
j=0
sum=0
l=[]

while n>0:
    for i in range(0, len(data)):
        if i != j:
            sum = sum + int(data[i])
    l.append(sum)
    j = j + 1
    sum = 0
    n-=1
print(min(l),max(l))
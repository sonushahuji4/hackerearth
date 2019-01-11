#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/repeated-k-times/description/

n=int(input())
data=list(map(int,input().split()))
k=int(input())
for i in range(n):
    d = int(min(data))
    countt=data.count(d)
    if countt==k:
        print(d)
        break
    else:
        data.remove(d)
#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/

T=int(input())
l=[]
while T>0:
    N, A, B = map(int, input().split())
    s=N
    for i in range(N+1):
        l.append(((A*(i*i))+(B*(s*s))))
        s-=1
    print(min(l))
    l.clear()
    T-=1
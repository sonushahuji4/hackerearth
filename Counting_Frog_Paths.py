#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/
x,y,s,t = list(map(int,input().split()))
a=0
for i in range(x,x+s+1):
    for j in range(y,y+s+1):
        if i+j<=t:
            a +=1
print(a)
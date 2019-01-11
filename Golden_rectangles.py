N=int(input())
x=1.6
y=1.7
flag=0
while N>0:
    a, b = map(int,input().split())
    s=a/b
    if x<=s and s<=y:
        flag+=1
    N-=1
print(flag)
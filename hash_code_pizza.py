R,M,L,H = map(int,input().split())
r=R
pizzadata = []
while r>0:
    pizzacell = list(map(str,input().split()))
    pizzadata.append(pizzacell)
    r -= 1
for eachcol in pizzadata:
    print(eachcol)
#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/easy-sum-set-problem-7e6841ca/
na = int(input())
a = sorted(map(int, input().split()))
nc = int(input())
c = sorted(map(int, input().split()))
b = []
for i in range(1, max(c) - max(a) + 1):
    for j in a:
        flag = False
        if (i + j) not in c:
            flag = True
            break
    if flag == False:
        b.append(i)

bsort = sorted(b)
for e in bsort:
    print(e, end=" ")

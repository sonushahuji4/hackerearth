#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/square-transaction-20/

t = int(input())
data = list(map(int, input().split()))
tn = int(input())
while tn > 0:
    sum = 0
    day = 0
    td = int(input())

    for i in data:
        flag = False
        sum = sum + i
        day += 1
        if sum >= td:
            print(day)
            flag = True
            break
    if flag == False:
        print(-1)
    tn -= 1

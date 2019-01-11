# problem link
# https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/min-max-difference/
T = int(input())
while T>0:
    N, M = map(int, input().split())
    test = N - M
    l = []
    l = list(map(int, input().split()))
    l.sort()
    datasize = len(l)
    flag = False
    count = 0
    if N == datasize:
        summdata = sum(l)
        maxdata = summdata
        mindata = summdata
        if flag == False:
            for i in l[::-1]:
                maxdata = maxdata - i
                count +=1
                if count == test:
                    flag = True
                    count = 0
                    break
        for i in range(datasize):
            mindata = mindata - l[i]
            count += 1
            if count == test:
                flag = False
                count = 0
                break
        print(mindata-maxdata)

    l.clear()
    T -= 1

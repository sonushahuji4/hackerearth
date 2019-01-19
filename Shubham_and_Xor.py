#problem statement
#https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/shubham-and-xor-8526868e/
T = int(input())
while T > 0:
    #datalist = list(map(int,input().split()))
    datalist = [int(x) for x in input().strip().split()]
    datasize = len(datalist)
    setofpairdata = []
    indexlocation = []
    pairs = []
    count = 0
    d = 0
    flag = False
    for i in range(datasize):
        j = i
        for j in range(j, datasize-1):
            d = j+1
            if datalist[i] == datalist[d] and i != d:
                if d not in indexlocation and i not in indexlocation:
                    indexlocation.append(d)
                    indexlocation.append(i)
                    setofpairdata.append(datalist[i])
                    break
        data = setofpairdata.count(datalist[i])
        if data == 1:
            pairs.append(data)
            setofpairdata.clear()
        elif data == 0:
            setofpairdata.clear()
    print(sum(pairs))
    T -= 1
# problem link
#https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/subset-and-4/
t = int(input())
while t > 0:
    flag = False
    z, l = map(int, input().split())
    s = list(map(int, input().split()))
    for i in range(0, l):
        for j in range(i + 1, l):
            m = s[i] & s[j]
            if z & m == 0:
                flag = True
                break
    if flag == True:
        print("Yes")
    else:
        print("No")
    t -= 1

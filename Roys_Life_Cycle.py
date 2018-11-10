#problem link
#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roys-life-cycle/
n = int(input())
l = []
X = 0
countx = 0
county = 0
while n > 0:
    text = input()
    Y = 0
    for i in range(0, len(text)):
        if text[i] == 'C':
            X += 1
            Y += 1
        else:
            X = 0
            Y = 0
        if countx < X:
            countx = X
        if county < Y:
            county = Y
    n -= 1
print(county, countx)


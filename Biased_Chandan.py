#problem link
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/biased-chandan/
n = int(input())
l = []
while n > 0:
    rate = int(input())

    if rate == 0:

        if l!=[]:
            l.pop()
    else:
        l.append(rate)
    n -= 1
sum = 0
for i in l:
    sum = sum + int(i)
print(sum)
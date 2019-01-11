# problem link
# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/bishu-and-soldiers/
n = int(input())
soldiers = []
for k in range(n):
    soldiers.append(int(input()))
r = int(input())
killed = 0
dead = 0
for i in range(r):
    killed = 0
    dead = 0
    power = int(input())
    l = power
    for j in soldiers:
        if j <= power:
            killed += 1
            dead = dead + j
        l -= 1
        if l == 0:
            break

    print(killed, dead)

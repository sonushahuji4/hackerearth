#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/breakup-app/
n = int(input())
data = []
while n > 0:
    d = input()
    data.append(d)
    n -= 1
w19 = 0
w21 = 0
for i in data:
    if '19' in i or '20' in i:
        w19 += 2

    if '21' in i:
        w21 += 1
if w19 > w21:
    print("Date")
elif w19 == w21:
    print("No Date")
else:
    print("No Date")

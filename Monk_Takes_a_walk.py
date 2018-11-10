#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/monk-takes-a-walk/

t = int(input())
flag = 0
alpha = []
while t > 0:
    alpha.append(input())
    t -= 1
for i in alpha:
    for ii in i:
        if ii is 'a' or ii is 'A' or ii is 'e' or ii is 'E' or ii is 'i' or ii is 'I' or ii is 'o' or ii is 'O' or ii is 'u' or ii is 'U':
            flag += 1

    print(flag)
    flag = 0
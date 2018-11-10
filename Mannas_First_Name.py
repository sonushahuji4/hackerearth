#problem link
#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/mannas-first-name-4/
t = int(input())

while t > 0:
    data = input()
    suvo = 0
    suvojit = 0
    for i in range(len(data)):
        if (data[i:i + 4]) == 'SUVO':
            suvo += 1
            if (data[i:i + 7]) == 'SUVOJIT':
                suvojit += 1
                suvo -= 1
    print('SUVO = {}, SUVOJIT = {}'.format(suvo, suvojit))
    t -= 1
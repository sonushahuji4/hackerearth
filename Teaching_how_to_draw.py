T = int(input())
for i in range(T):
    S = int(input())
    numberOfWays = 0
    for j in range(1, int(S ** 0.5) + 1):
        numberOfWays += int(S / j) - (j - 1)
    print(numberOfWays)
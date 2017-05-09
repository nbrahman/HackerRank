def solutionCounterGame(n):
    count = 0
    n -= 1
    while (n > 0):
        n &= (n - 1)
        count += 1
    if count & 1:
        return 'Louise'
    else:
        return 'Richard'

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(solutionCounterGame(n))
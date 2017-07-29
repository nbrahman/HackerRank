def solutionManasaAndStones(n, diff1, diff2):
    res = set()
    for i in range(n):
        res.add(diff1 * i + diff2 * (n - i - 1))
    res = list(res)
    res.sort()
    return map(str, res)


q = int(input().strip())
for _ in range(q):
    numberOfStones = int(input().strip())
    diff1 = int(input().strip())
    diff2 = int(input().strip())
    print(' '.join(solutionManasaAndStones(numberOfStones, diff1, diff2)))
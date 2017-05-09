import sys

n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    pset = set()
    p = ''
    res = 0
    for i in s:
        if i not in pset:
            res += 1
            pset.add(i)
    print(res)
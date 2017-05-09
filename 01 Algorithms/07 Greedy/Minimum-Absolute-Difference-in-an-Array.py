# !/bin/python3

from sys import maxsize


def calculateMinimumAbsDiff(a):
    a.sort()
    min = maxsize
    for i in range(len(a)-1):
        if abs(a[i]-a[i + 1]) < min:
            min = abs(a[i]-a[i + 1])
    return min


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here
print(calculateMinimumAbsDiff(a))
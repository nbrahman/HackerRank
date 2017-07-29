#!/bin/python3

from math import floor

def countSpecialProblems(n , k, t):
    cnt, page = 0, 1
    for chapter in t:
        for p in range(1, chapter + 1):
            if p == page:
                cnt += 1
            if p != chapter and p % k == 0:
                page += 1
        page += 1
    return cnt




n,k = map(int, input().strip().split(' '))
t = list(map(int, input().strip().split(' ')))
print(countSpecialProblems(n, k, t))
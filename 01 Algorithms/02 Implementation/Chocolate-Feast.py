#!/bin/python3

import sys

def countChocolates(n, c, m):
    cntChocolates = n / c
    cntWrappers = cntChocolates
    while cntWrappers >= m:
        cntWrappers = cntWrappers - m
        cntChocolates += 1
        cntWrappers += 1
    return int(cntChocolates)



t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    print(countChocolates(n, c, m))

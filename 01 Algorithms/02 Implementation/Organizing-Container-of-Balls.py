#!/bin/python3

import sys


def colsum (M):
    l = [0] * len(M[0])
    for i in range(len(M[0])):
        for j in range(len(M)):
            l[i] += M[j][i]
    return l

def rowsum (M):
    l = [0] * len(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            l[i] += M[i][j]
    return l


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
       M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
       M.append(M_t)
    cs = colsum(M)
    rs = rowsum(M)

    cs.sort()
    rs.sort()
    i = 0
    while i < n and cs[i] == rs[i]:
        i += 1

    if i == n:
        print('Possible')
    else:
        print('Impossible')

#!/bin/python3

from math import ceil

def countSpecialProblems(n , k, t):
    cnt, offset = 0, 1
    for chapter in t:
        pages = ceil((chapter + k - 1) / k)
        #print(pages)
        for i in range(pages):
            if offset >= (i * k) and offset <= min((i + 1) * k, chapter):
                cnt += 1
            offset += 1
    return cnt




n,k = map(int, input().strip().split(' '))
t = list(map(int, input().strip().split(' ')))
print(countSpecialProblems(n, k, t))
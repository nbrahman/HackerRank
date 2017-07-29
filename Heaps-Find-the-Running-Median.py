#!/bin/python3

import sys


n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    a.sort()
    if len(a) % 2 == 1:
        print(float(a[int(len(a) // 2)]))
    else:
        print((a[int(len(a) / 2)] + a[int(len(a) / 2) - 1]) / 2)
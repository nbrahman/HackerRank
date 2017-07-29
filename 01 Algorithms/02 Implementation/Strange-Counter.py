#!/bin/python3

import sys

t = int(input().strip())

total = 0
n = 3
while total < t:
    total += n
    n *= 2
n /= 2
print(total - t + 1)
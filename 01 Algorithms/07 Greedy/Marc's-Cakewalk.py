#!/bin/python3

import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
# your code goes here
m = 0
calories.sort(reverse=True)
for i in range(n):
    m += calories[i] * (2 ** i)
print (m)
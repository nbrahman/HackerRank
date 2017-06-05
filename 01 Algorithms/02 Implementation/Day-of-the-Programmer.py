#!/bin/python3

import sys

def solve(year):
    if year == 1918:
        l = [31, 15, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1700 <= year < 1918:
        if year % 4 == 0:
            l[1] = 29
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            l[1] = 29

    day = 256
    print(l)
    i = 0
    while i < len(l) and day - l[i]>= 0:
        if day - l[i] >= 0:
            day -= l[i]
        i += 1
    return "{0:0>2}.{1:0>2}.{2}".format(day, i + 1, year)



year = int(input().strip())
result = solve(year)
print(result)

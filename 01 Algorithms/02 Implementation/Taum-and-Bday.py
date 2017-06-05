#!/bin/python3

import sys


def solution (b, w, x, y, z):
    if x < z and y < z:
        return b * x + w * y
    elif x + z < y:
        return b * x + w * (x + z)
    elif y + z < x:
        return b * (y + z) + w * y
    else:
        return b * x + w * y

t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print (solution(b, w, x, y, z))
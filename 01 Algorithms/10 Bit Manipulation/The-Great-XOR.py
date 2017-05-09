#!/bin/python3

import sys

def theGreatXor(x):
    # Complete this function
    b = format(x, 'b')
    l = len(b)-1
    s = 0
    for i in range(len(b)):
        if b[i]=='0':
            s += 2 ** (l - i)
    return s

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = theGreatXor(x)
    print(result)

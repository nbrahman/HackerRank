#!/bin/python3

import sys

def super_reduced_string(s):
    l = []
    for i in range(len(s)):
        if not l or s[i] != l[-1]:
            l += [s[i]]
        else:
            l.pop()
    if l:
        return ''.join(l)
    else:
        return 'Empty String'


s = input().strip()
result = super_reduced_string(s)
print(result)

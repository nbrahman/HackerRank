#!/bin/python3

import sys

def validateNewString(s):
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            return False
    return True

def solution(s):
    st = list(set(s))
    retValue = 0
    for i in range(len(st)):
        for j in range(i + 1, len(st)):
            newString = []
            for t in s:
                if t == st[i] or t == st[j]:
                    newString.append(t)
            if validateNewString(newString):
                retValue = max (retValue, len(newString))
    return retValue

s_len = int(input().strip())
s = input().strip()
print(solution(s))
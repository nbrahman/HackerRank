#!/bin/python3

import sys

def solution(s, n):
    retValue = []
    for t in s:
        if t.isalpha():
            retValue.append(chr(ord(t)+n))
        else:
            retValue.append(t)
    return ''.join(retValue)




n = int(input().strip())
s = input().strip()
k = int(input().strip())
print(solution(s, k))


k = 2
k = k%26
n = 11
s = "middle-Outz"

chars_list = list(list(map(chr, range(65, 91))) + list(map(chr, range(65, 91))))[0:k] + \
             list(list(map(chr, range(97, 123))) + list(map(chr, range(97, 123))))[0:k]

print (chars_list)
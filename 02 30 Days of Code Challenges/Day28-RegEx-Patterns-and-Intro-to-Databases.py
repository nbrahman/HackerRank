#!/bin/python3

import sys
import re

l = []
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search(r'[\w\.-]+@gmail\.com',emailID) != None:
        l.append(firstName)
l = sorted(l)
for i in l:
    print(i)
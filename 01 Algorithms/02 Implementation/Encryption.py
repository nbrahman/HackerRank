#!/bin/python3

import sys
import math as m


s = input().replace(" ","")
c = int(m.ceil(m.sqrt(len(s))))
for a in range(c):
    print(s[a::c], end=' ')
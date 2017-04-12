'''
Consider two sets of positive integers, A={a0,a1,...an-1} and B={b0,b1,...bm-1}. We say that a positive integer, x, is between sets A and B if the following conditions are satisfied:

    All elements in A are factors of x.
    x is a factor of all elements in B.

Given A and B, find and print the number of integers (i.e., possible x's) that are between the two sets.

Input Format

The first line contains two space-separated integers describing the respective values of n (the number of elements in set A) and m (the number of elements in set B).
The second line contains n distinct space-separated integers describing a0,a1,....,an-1.
The third line contains m distinct space-separated integers describing b0,b1,....,bm-1.

Constraints
1<=n,m<=10
1<=ai<=100
1<=bi<=100

Output Format

Print the number of integers that are considered to be between A and B.

Sample Input

2 3
2 4
16 32 96

Sample Output

3

Explanation

The integers that are between A={2,4} and B={16, 32, 96} are 4, 8, and 16.
'''
#!/bin/python3

import sys
from functools import reduce

def gcd(a,b):
    while (b):
        a,b = b, a%b
    return a

def lcm(a,b):
    return (a*b)/gcd(a,b)

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
gcdB=reduce(gcd,b)
lcmA=int(reduce(lcm,a))
cnt=0
for i in range (lcmA,gcdB+1,lcmA):
    if gcdB % i == 0:
        cnt+=1
print (cnt)
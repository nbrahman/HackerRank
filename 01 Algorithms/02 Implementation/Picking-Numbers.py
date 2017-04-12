'''
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is <=1.

Input Format

The first line contains a single integer, n, denoting the size of the array.
The second line contains n space-separated integers describing the respective values of a0,a1,...,an-1.

Constraints
2<=n<=100
0<=ai<=100
The answer will be >=2.

Output Format

A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is <=1.

Sample Input 0

6
4 6 5 3 3 1

Sample Output 0

3

Explanation 0

We choose the following multiset of integers from the array: {4,3,3}. Each pair in the multiset has an absolute difference <=1(i.e.|4-3|=1, and |3-3|=0), so we print the number of chosen integers, 3, as our answer.

Sample Input 1

6
1 2 2 3 1 2

Sample Output 1

5

Explanation 1

We choose the following multiset of integers from the array: {1,2,2,1,2}. Each pair in the multiset has an absolute difference <=1(i.e.|1-2|=1, |1-1|=0, and |2-2|=0), so we print the number of chosen integers, 5, as our answer.
'''


#!/bin/python3

import sys
from collections import Counter

def solution (a):
    c=Counter (a)
    k=(list(c.keys()))
    cnt=0
    if len(k)<=1:
        cnt=c.get(k[0])
    else:
        for i in range(len(k)-1):
            if cnt<c.get(k[i]):
                cnt=c.get(k[i])
            if abs(k[i]-k[i+1])<=1:
                if cnt<c.get(k[i])+c.get(k[i+1]):
                    cnt=c.get(k[i])+c.get(k[i+1])
    print(cnt)

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
solution(a)
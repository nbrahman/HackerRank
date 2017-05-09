'''
Consider an array of n integers, A=[a<0>, a<1>, a<2>, ..., a<n-1>]. The distance between two indices, i and j, is denoted by d<i,j> = |i - j|.

Given A, find the minimum d<i,j> such that a<i>=a<j> and i != j. In other words, find the minimum distance between any pair of equal elements in the array. If no such value exists, print -1.

Note: |a| denotes the absolute value of a.

Input Format

The first line contains an integer, n, denoting the size of array A.
The second line contains n space-separated integers describing the respective elements in array A.

Constraints
1<=n<=10^3
1<=a<i><=10^5

Output Format

Print a single integer denoting the minimum d<i,j> in A; if no such value exists, print -1.

Sample Input

6
7 1 3 4 1 7

Sample Output

3

Explanation
Here, we have two options:
a<1> and a<4> are both 1, so d<1,4> = |1-4|=3.
a<0> and a<5> are both 7, so d<0,5> = |0-5|=5.

The answer is min(3,5)=3.
'''
# !/bin/python3

import sys

def calculateMinimumDistance(a):
    min = 1000000000
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                if min > abs(i - j):
                    min = abs(i - j)
    if min == 1000000000:
        min = -1
    return min


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
print(calculateMinimumDistance(A))
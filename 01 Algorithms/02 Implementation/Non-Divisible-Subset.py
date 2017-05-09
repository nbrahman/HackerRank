'''
Given a set, S, of n distinct integers, print the size of a maximal subset, S', of S where the sum of any 2 numbers in S' is not evenly divisible by k.

Input Format

The first line contains 2 space-separated integers, n and k, respectively.
The second line contains n space-separated integers (we'll refer to the ith value as a<i>) describing the unique values of the set.

Constraints
1<=n<=10^5
1<=k<=100
1<=a<i><=10^9
All of the given numbers are distinct.

Output Format

Print the size of the largest possible subset (S').

Sample Input

4 3
1 7 2 4

Sample Output

3

Explanation

The largest possible subset of integers is S'={1,7,4}, because no two integers will have a sum that is evenly divisible by k=3:

1+7=8, and is not evenly divisible by 3.
1+4=5, and is not evenly divisible by 3.
4+7=11, and is not evenly divisible by 3.

The number 2 cannot be included in our subset because it will produce an integer that is evenly divisible k=3 by when summed with any of the other integers in our set:

1+2=3, and 3/3=1(remainder=0).
4+2=6, and 6/3=2(remainder=0).
7+2=9, and 9/3=3(remainder=0).

Thus, we print the length of S' on a new line, which is 3.
'''


#!/bin/python3

import sys

def Solution (a,k):
    d={}
    for i in a:
        d[i%k]=d.get(i%k,0)+1
    cnt=0
    i=0
    while(i*2<=k):
        opp=(k-i)%k
        if (i==opp):
            cnt+=min(d.get(i,0),1)
        else:
            cnt+=max(d.get(i,0),d.get(opp,0))
        i+=1
    print (cnt)



n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
Solution(a, k)
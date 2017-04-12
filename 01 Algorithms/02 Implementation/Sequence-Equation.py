'''
You are given a sequence of n integers, p(1),p(2),...,p(n). Each element in the sequence is distinct and satisfies 1<=p(x)<=n. For each x where 1<=x<=n, find any integer y such that p(p(y))=x and print the value of y on a new line.

Input Format

The first line contains an integer, n, denoting the number of elements in the sequence.
The second line contains n space-separated integers denoting the respective values of p(1),p(2),...,p(n).

Constraints
1<=n<=50
1<=p(x)<=50, where 1<=x<=n.
Each element in the sequence is distinct.

Output Format

For each x from 1 to n, print an integer denoting any valid y satisfying the equation p(p(y))=x on a new line.

Sample Input 0

3
2 3 1

Sample Output 0

2
3
1

Explanation 0

Given the values of p(1)=2, p(2)=3, and p(3)=1, we calculate and print the following values for each x from 1 to n:

1. x=1=p(3)=p(p(2))=p(p(y)), so we print the value of y=2 on a new line.
2. x=2=p(1)=p(p(3))=p(p(y)), so we print the value of y=3 on a new line.
3. x=3=p(2)=p(p(1))=p(p(y)), so we print the value of y=1 on a new line.

'''

#!/bin/python3

import sys

def SequenceEquationSolution(n,a):
    for x in range(n):
        print(a.index(a.index(x+1)+1)+1)


n = int(input().strip())
line=sys.stdin.readlines()
a=[int(a_temp) for a_temp in line[0].strip().split(' ')]
SequenceEquationSolution(n,a)


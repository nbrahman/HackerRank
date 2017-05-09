'''
We say that a string, s, contains the word hackerrank if a subsequence of the characters in s spell the word hackerrank. For example, haacckkerrannkk does contain hackerrank, but haacckkerannk does not (the characters all appear in the same order, but it's missing a second r).

More formally, let p<0>, p<1>,...p<9> be the respective indices of h, a, c, k, e, r, r, a, n, k in string s. If p<0> < p<1> < p<2> < ... <p<9> is true, then s contains hackerrank.

You must answer q queries, where each query i consists of a string, s<i>. For each query, print YES on a new line if contains hackerrank; otherwise, print NO instead.

Input Format

The first line contains an integer denoting q(the number of queries).
Each line i of the q subsequent lines contains a single string denoting s<i>.

Constraints
2<=q<=10^2
10<=|s<i>|<=10^4

Output Format

For each query, print YES on a new line if s<i> contains hackerrank; otherwise, print NO instead.

Sample Input 0

2
hereiamstackerrank
hackerworld

Sample Output 0

YES
NO

Explanation 0

We perform the following q=2 queries:

s=hereiamstackerrank
    The characters of hackerrank are bolded in the string above. Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we print YES on a new line.
s=hackerworld does not contain the last four characters of hackerrank, so we print NO on a new line.
'''

#!/bin/python3

import sys


q = int(input().strip())
l = 'hackerrank'
for a0 in range(q):
    s = input().strip()
    # your code goes here
    if len(s) < len(l):
        print('NO')
    else:
        prevPos = -1
        flg = False
        for a in l:
            try:
                currPos=s.index(a,prevPos+1)
                if currPos > prevPos:
                    prevPos = currPos
                    flg = True
                else:
                    flg = False
                    break
            except(ValueError):
                flg = False
                break
        if flg == False:
            print('NO')
        else:
            print('YES')
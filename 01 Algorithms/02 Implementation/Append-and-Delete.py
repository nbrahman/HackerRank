'''
You have a string, s, of lowercase English alphabetic letters. You can perform two types of operations on s:

    Append a lowercase English alphabetic letter to the end of the string.
    Delete the last character in the string. Performing this operation on an empty string results in an empty string.

Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. If it's possible, print Yes; otherwise, print No.

Input Format

The first line contains a string, s, denoting the initial string.
The second line contains a string, t, denoting the desired final string. The third line contains an integer, k, denoting the desired number of operations.

Constraints
1<=|s|,|k|,t<=100
s and t consist of lowercase English alphabetic letters.

Output Format

Print Yes if you can obtain string t by performing exactly k operations on s; otherwise, print No.

Sample Input 0

hackerhappy
hackerrank
9

Sample Output 0

Yes

Explanation 0

We perform 5 delete operations to reduce string s to hacker. Next, we perform 4 append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert s to t by performing exactly k=9 operations, we print Yes.

Sample Input 1

aba
aba
7

Sample Output 1

Yes

Explanation 1

We perform 4 delete operations to reduce string s to the empty string (recall that, though the string will be empty after 3 deletions, we can still perform a delete operation on an empty string to get the empty string). Next, we perform 3 append operations (i.e., a, b, and a). Because we were able to convert s to t by performing exactly k=7 operations, we print Yes.
'''

#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        break

if ((len(s) + len(t) - 2 * i <= k) and (
        (len(s) + len(t) - 2 * i) % 2 == k % 2)) or (len(s) + len(t) < k):
    print("Yes")
else:
    print("No")
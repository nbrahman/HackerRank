'''
John's clothing store has a pile of n loose socks where each sock i is labeled with an integer, ci, denoting its color. He wants to sell as many socks as possible, but his customers will only buy them in matching pairs. Two socks, i and j, are a single matching pair if ci=cj.

Given n and the color of each sock, how many pairs of socks can John sell?

Input Format

The first line contains an integer, n, denoting the number of socks.
The second line contains space-separated integers describing the respective values of c0,c1,...,cn-1.

Constraints
1<=n<=100
1<=ci<=100
Output Format

Print the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20

Sample Output

3

Explanation

sock.png

As you can see from the figure above, we can match three pairs of socks. Thus, we print on a new line.
'''
#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d={}
cnt=0
for i in c:
    d[i] = d.get (i,0)+1
    if d.get(i,0)%2==0:
        cnt+=1
print (cnt)

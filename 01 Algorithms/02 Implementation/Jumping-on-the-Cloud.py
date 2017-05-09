'''
Emma is playing a new mobile game involving n clouds numbered from 0 to n-1. A player initially starts out on cloud c<0>, and they must jump to cloud c<n-1>. In each step, she can jump from any cloud i to cloud i+1 or cloud i+2.

There are two types of clouds, ordinary clouds and thunderclouds. The game ends if Emma jumps onto a thundercloud, but if she reaches the last cloud (i.e., c<n-1>), she wins the game!

[jump(1).png]

Can you find the minimum number of jumps Emma must make to win the game? It is guaranteed that clouds c<0> and c<n-1> are ordinary-clouds and it is always possible to win the game.

Input Format

The first line contains an integer, n(the total number of clouds).
The second line contains n space-separated binary integers describing clouds c<0>,c<1>,...,c<n-1>.

    If c<i>=0, the ith cloud is an ordinary cloud.
    If c<i>=1, the ith cloud is a thundercloud.

Constraints
2<=n<=100
c<i>=[0,1]
c<0>=c<n-1>=0

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0

Sample Output 0

4

Sample Input 1

6
0 0 0 0 1 0

Sample Output 1

3

Explanation

Sample Case 0:
Because c<2> and c<5> in our input are both 1, Emma must avoid c<2> and c<5>. Bearing this in mind, she can win the game with a minimum of 4 jumps:

[jump(2).png]

Sample Case 1:
The only thundercloud to avoid is c<4>. Emma can win the game in 3 jumps:

[jump(5).png] 
'''

#!/bin/python3

import sys

def Solution(c):
    cnt=0
    i=0
    while i<n-1:
        if i+2<n and c[i+2]==0:
            i+=2
        else:
            i+=1
        cnt+=1
    print(cnt)


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
Solution(c)
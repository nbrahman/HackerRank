'''
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where s is the start point and t is the end point. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point a and the orange tree is at point b.

Apple and orange(2).png

When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right.

Given the value of d for m apples and n oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t])? Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your second line of output.

Input Format

The first line contains two space-separated integers denoting the respective values of s and t.
The second line contains two space-separated integers denoting the respective values of a and b.
The third line contains two space-separated integers denoting the respective values of m and n.
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

Constraints
1<=s,t,a,b,m,n<=10^5
-10^5<=d<=10^5
a<s<t<b

Output Format

Print two lines of output:

    On the first line, print the number of apples that fall on Sam's house.
    On the second line, print the number of oranges that fall on Sam's house.

Sample Input 0

7 11
5 15
3 2
-2 2 1
5 -6

Sample Output 0

1
1

Explanation 0

The first apple falls at position 5-2=3.
The second apple falls at position 5+2=7.
The third apple falls at position 5+1=6.
The first orange falls at position 15+5=20.
The second orange falls at position 15-6=9.
Only one fruit (the second apple) falls within the region between 7 and 11, so we print 1 as our first line of output.
Only the second orange falls within the region between 7 and 11, so we print 1 as our second line of output.
'''

#!/bin/python3

import sys

def checkRange (s,t,loc,l):
    withinRangeCounter = 0
    for i in range (len(l)):
        if (loc+l[i]>=s) and (loc+l[i]<=t):
            withinRangeCounter+=1
    print(withinRangeCounter)

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
checkRange(s,t,a,apple)
checkRange(s,t,b,orange)

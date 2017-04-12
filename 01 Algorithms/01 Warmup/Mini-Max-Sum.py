'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints

    Each integer is in the inclusive range [1, 10^9].

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

Sample Input

1 2 3 4 5

Sample Output

10 14

Explanation

Our initial numbers are , , , , and . We can calculate the following sums using four of the five integers:

    If we sum everything except 1, our sum is 2+3+4+5=14.
    If we sum everything except 2, our sum is 1+3+4+5=13.
    If we sum everything except 3, our sum is 1+2+4+5=12.
    If we sum everything except 4, our sum is 1+2+3+5=11.
    If we sum everything except 5, our sum is 1+2+3+4=10.

As you can see, the minimal sum is 1+2+3+4=10 and the maximal sum is 2+3+4+5=14. Thus, we print these minimal and maximal sums as two space-separated integers on a new line.

Hints: Beware of integer overflow! Use 64-bit Integer.
'''
#!/bin/python

import sys


#a,b,c,d,e = input().strip().split(' ')
#a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
l = [int(a_temp) for a_temp in input().strip().split(' ')]
l.sort()
max = 0
min = 0
for i in range(1,len(l)):
    max += l[i]
min = max + l[0] - l[len(l)-1]
print (min, max)
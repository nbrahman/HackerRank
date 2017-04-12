'''
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

    If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0).
    If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15 Hackos * (the number of days late).
    If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine=500 Hackos * (the number of months late).
    If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Input Format

The first line contains 3 space-separated integers denoting the respective day, month, and year on which the book was actually returned.
The second line contains 3 space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).

Constraints
1<=D<=31
1<=M<=12
1<=Y<=3000
It is guaranteed that the dates will be valid Gregorian calendar dates
Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015

Sample Output

45

Explanation

Given the following return dates:
Actual:D<a>=9,M<a>=6,Y<a>=2015
Expected:D<e>=6,M<e>=6,Y<a>=2015

Because Y<a>=Y<e>, we know it is less than a year late.
Because M<A>=M<e>, we know it's less than a month late.
Because D<e><D<a>, we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be 15 Hackos * (# days late). We then print the result of 15*(D<a>-D<e>)=15*(9-6)=45 as our output.
'''
#!/bin/python3

import sys
from datetime import date


def Solution(da,ma,ya,de,me,ye):
    e = date(ye,me,de)
    a = date(ya,ma,da)
    fine=0
    if a.day>e.day and a.month==e.month and a.year==e.year:
        fine=(a.day - e.day) * 15
    if a.month>e.month and a.year==e.year:
        fine=(a.month-e.month)*500
    if a.year>e.year:
        fine=10000
    return fine

d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]
print(Solution(d1,m1,y1,d2,m2,y2))
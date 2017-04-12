'''
Brie’s Drawing teacher asks her class to open their n-page book to page number p. Brie can either start turning pages from the front of the book (i.e., page number 1) or from the back of the book (i.e., page number n), and she always turns pages one-by-one (as opposed to skipping through multiple pages at once). When she opens the book, page 1 is always on the right side:

image

Each page in the book has two sides, front and back, except for the last page which may only have a front side depending on the total number of pages of the book (see the Explanation sections below for additional diagrams).

Given n and p, find and print the minimum number of pages Brie must turn in order to arrive at page p.

Input Format

The first line contains an integer, n, denoting the number of pages in the book.
The second line contains an integer, p, denoting the page that Brie's teacher wants her to turn to.

Constraints
1<=n<=10^5
1<=p<=n

Output Format

Print an integer denoting the minimum number of pages Brie must turn to get to page p.

Sample Input 0

6
2

Sample Output 0

1

Explanation 0

If Brie starts turning from page 1, she only needs to turn 1 page:
1->2/3

Untitled Diagram(6).png

If Brie starts turning from page 6, she needs to turn 2 pages:
6->4/5->2/3

Untitled Diagram(3).png

Because we want to print the minumum number of page turns, we print 1 as our answer.

Sample Input 1

5
4

Sample Output 1

0

Explanation 1

If Brie starts turning from page 1, she needs to turn 2 pages:
1->2/3->4/5

Untitled Diagram(4).png

If Brie starts turning from page 5, she doesn't need to turn any pages:
4/5

Untitled Diagram(5).png

Because we want to print the minimum number of page turns, we print 0 as our answer.
'''
#!/bin/python3

import sys

def solve(n, p):
    flg = False
    i=0
    while (i<n//2) and (flg==False):
        if (p==2*i) or (p==(2*i+1)):
            flg=True
        if n%2==0:
            if (p==n-(2*i)) or (p==(n-(2*i)+1)):
                flg=True
        else:
            if (p==n-(2*i)) or (p==(n-(2*i)-1)):
                flg=True
        i+=1
    if i-1<0:
        i=0
    else:
        i-=1
    return i


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)

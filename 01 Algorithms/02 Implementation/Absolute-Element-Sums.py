'''
Given an array, A, of N integers, you must answer Q queries. Each query consists of a single integer, x, and is performed as follows:

    Add x to each element of the array, permanently modifying it for any future queries.
    Find the absolute value of each element in the array and print the sum of the absolute values on a new line.

Tip: The Input/Output for this challenge is very large, so you'll have to be creative in your approach to pass all test cases.

Input Format

The first line contains an integer, N(the number of elements in array ).
The second line contains N space-separated integers describing each element i in array A.
The third line contains Q(the number of queries).
The fourth line contains Q space-separated integers (describing each x<j>).

Constraints
1<=N,Q<=5*10^5
-2000<=A[i]<=2000, where 0<=i<N and A is the array of size N.
-2000<=x[j]<=2000, where 0<=j<Q 

Output Format

For each query, print the sum of the absolute values of all the array's elements on a new line.

Sample Input

3
-1 2 -3
3
1 -2 3 

Sample Output

5
7
6

Explanation

Query 0:x=1
Array:[-1,2,-3]->[0,3,-2]
The sum of the absolute values of the updated array's elements is |0|+|3|+|-2|=0+3+2=5, so we print 5 on a new line.

Query 1:x=-2
Array:[0,3,-2]->[-2,1,-4]
The sum of the absolute values of the updated array's elements is |-2|+|1|+|-4|=2+1+4=7, so we print 7 on a new line.

Query 2:x=3
Array:[-2,1,-4]->[1,4,-1]
The sum of the absolute values of the updated array's elements is |1|+|4|+|-1|=1+4+1=6, so we print 6 on a new line.
'''

n = input().strip()
n = int(n)
a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
q = input().strip()
q = int(n)
x = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in x:
    s=0
    for j in range(len(a)):
        a[j]+=i
        s+=abs(a[j])
    print(s)

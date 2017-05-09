'''
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

Input Format

The first line contains an integer, n, denoting the number of elements in the array.
The second line contains n space-separated integers describing the array's elements.

Constraints
5<=n<=50
0<=x<i><=100, where x<i> is the ith element of the array.

Output Format

Print 3 lines of output in the following order:

    The first line should be the value of Q1.
    The second line should be the value of Q2.
    The third line should be the value of Q3.

Sample Input

9
3 7 8 5 12 14 21 13 18

Sample Output

6
12
16

Explanation

X={3,7,8,5,12,14,21,13,18}. When we sort the elements in non-decreasing order, we get X={3,5,7,8,12,13,14,18,21}. It's easy to see that median(X)=12.

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:

    Lower half (L): 3, 5, 7, 8

    Upper half (U): 13, 14, 18, 21

Now, we find the quartiles:

Q1 is the meadian(L). So, (5+7)/2=6.
Q2 is the meadian(X). So, 12.
Q3 is the meadian(U). So, (14+18)/2=16.
'''


class Quartiles(object):
    def calculateQuartiles (self, x):
        x.sort()
        lx=x[0:int(len(x)/2)]
        if len(x)%2==0:
            ux=x[int(len(x)/2):]
        else:
            ux=x[int(len(x)/2)+1:]

        print(self.calculateMedian(len(lx),lx))
        print(self.calculateMedian(len(x),x))
        print(self.calculateMedian(len(ux),ux))


    def calculateMedian(self,n,x):
        if n%2==0:
            return int((x[int(n/2)-1]+x[int(n/2)])/2)
        else:
            return int(x[int(n/2)])


if __name__ == '__main__':
    n = input().strip()
    n = int(n)
    x = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    m = Quartiles()
    m.calculateQuartiles (x)
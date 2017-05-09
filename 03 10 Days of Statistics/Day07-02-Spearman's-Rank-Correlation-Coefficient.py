'''
Objective
In this challenge, we practice calculating Spearman's rank correlation coefficient. Check out the Tutorial tab for learning materials!

Task
Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.

Input Format

The first line contains an integer, n, denoting the number of values in data sets X and Y.
The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X.
The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y.

Constraints
10<=n<=100
1<=x<i><=500, where x<i> is the value of data set X.
1<=y<i><=500, where y<i> is the value of data set Y.
Data set X contains unique values.
Data set Y contains unique values.


Output Format

Print the value of the Spearman's rank correlation coefficient, rounded to a scale of 3 decimal places.

Sample Input

10
10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
200 44 32 24 22 17 15 12 8 4

Sample Output

0.903

Explanation

We know that data sets X and Y both contain unique values, so the rank of each value in each data set is unique. Because of this property, we can use the following formula to calculate the value of Spearman's rank correlation coefficient:
r<x,y>=1-((6-sum(d<i>^2))/(N-(N^2-1)))
Here, d<i> is the difference between ranks of each pair (x<i>, y<i>). The following table shows the calculation of d<i>^2:
x       y       r<x>        r<y>        d<i>=r<x>-r<y>      d<i>^2
10      200     10          10          0                   0
9.8     44      9           9           0                   0
8       32      8           8           0                   0
7.8     24      7           7           0                   0
7.7     22      6           6           0                   0
1.7     17      2           5           -3                  9
6       15      5           4           1                   1
5       12      4           3           1                   1
1.4     8       1           2           -1                  1
2       4       3           1           2                   4

Now, we find the value of the coefficient:
r<x,y>=1-((6*16)/(10*99))=1-0.09696969696=0.90303030303

When rounded to a scale of three decimal places, we get 0.903 as our final answer.
'''


def calculateSpearmanRankCorrelationCoefficient(n, x, y, d):
    s = 0
    x_s = x.copy()
    y_s = y.copy()
    x_s.sort()
    y_s.sort()
    for i in range(n):
        s += ((x_s.index (x[i])-y_s.index(y[i]))**2)
    print(round(1-((6 * s)/(n * ((n ** 2)-1))), d))

n = int(input().strip())
x = list(map(float, input().strip().split(' ')))
y = list(map(float, input().strip().split(' ')))
calculateSpearmanRankCorrelationCoefficient(n, x, y, 3)
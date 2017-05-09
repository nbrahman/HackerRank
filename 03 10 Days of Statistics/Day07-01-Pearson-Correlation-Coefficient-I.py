'''
Objective
In this challenge, we practice calculating the Pearson correlation coefficient. Check out the Tutorial tab for learning materials!

Task
Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

Input Format

The first line contains an integer, n, denoting the size of data sets x and y.
The second line contains n space-separated real numbers (scaled to at most one decimal place), defining data set X.
The third line contains n space-separated real numbers (scaled to at most one decimal place), defining data set Y.

Constraints
10<=n<=100
1<=x<i><=500, where x<i> is the value of data set X.
1<=y<i><=500, where y<i> is the value of data set Y.
Data set X contains unique values.
Data set Y contains unique values.

Output Format

Print the value of the Pearson correlation coefficient, rounded to a scale of 3 decimal places.

Sample Input

10
10 9.8 8 7.8 7.7 7 6 5 4 2 
200 44 32 24 22 17 15 12 8 4

Sample Output

0.612

Explanation

The mean and standard deviation of data set X are: 6.73 and 2.39251

The mean and standard deviation of data set are: 37.8 and 55.1993

We use the following formula to calculate the Pearson correlation coefficient:
    correlation<x,y>=sum((x<i>-mean<x)*(y<i>-mean<y>))/(n*<stddev<x>*stddev<y>)
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT


def calculateMean(x):
    return(sum(x) / len(x))

def calculateStandardDeviation(x, m):
    l = []
    for i in range(len(x)):
        l.append((x[i]-m)**2)
    return ((sum(l) / len(l)) ** 0.5)

def calculatePearsonCorrelationCoefficient(n, x, y, d):
    meanX = calculateMean(x)
    meanY = calculateMean(y)
    stddevX = calculateStandardDeviation(x, meanX)
    stddevY = calculateStandardDeviation(y, meanY)
    numerator = 0
    for i in range(n):
        numerator = numerator + ((x[i] - meanX) * (y[i] - meanY))
    print(round(numerator / (n * stddevX * stddevY), d))

n = int(input().strip())
x = list(map(float, input().strip().split(' ')))
y = list(map(float, input().strip().split(' ')))
calculatePearsonCorrelationCoefficient(n, x, y, 3)
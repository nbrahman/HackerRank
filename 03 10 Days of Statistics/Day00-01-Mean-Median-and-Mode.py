'''
Objective
In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, X, of N integers, calculate and print the the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of decimal place (i.e., 12.3, 7.0 format).

Input Format

The first line contains an integer, N, denoting the number of elements in the array.
The second line contains N space-separated integers describing the array's elements.

Constraints
10<=N<=2500
0<=x<i><=10^5, where x<i> is the ith element of the array.

Output Format

Print 3 lines of output in the following order:

    Print the mean on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
    Print the median on a new line, to a scale 1 of decimal place (i.e., 12.3, 7.0).
    Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output

43900.6
44627.5
4978

Explanation

Mean:
We sum all N elements in the array, divide the sum by N, and print our result on a new line.

Median:
To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order. The sorted array X={4978, 11735, 14216, 14470, 38120, 51135, 64630, 67060, 73429, 99233}. We then average the two middle elements:
median=(x<4>+x<5>)/2=89255/2=44627.5
and print our result on a new line.

Mode:
We can find the number of occurrences of all the elements in the array:

 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1

Every number occurs once, making 1 the maximum number of occurrences for any number in X. Because we have multiple values to choose from, we want to select the smallest one, 4978, and print it on a new line.
'''

from collections import Counter

class MeanMedianMode(object):
    def calculateMeanMedianMode (self, x):
        self.calculateMean(x,1)
        self.calculateMedian(x,1)
        self.calculateMode(x,1)

    def calculateMean (self,x,d):
        print(round(sum(x)/len(x),d))

    def calculateMedian (self,x,d):
        x=sorted(x)
        if len(x) < 1:
            print(None)
        if len(x) % 2 == 1:
            print(round(x[((len(x) + 1) / 2) - 1],d))
        else:
            print(round(float(sum(x[int(len(x) / 2) - 1:int(len(x) / 2) + 1])) / 2.0,d))

    def calculateMode (self,x,d):
        c=Counter(x)
        most_common = sorted(c.items(),key=lambda pair: (-pair[1], int(pair[0])))
        print(round(most_common[0][0],1))


if __name__ == '__main__':
    n = input().strip()
    n = int(n)
    x = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    m = MeanMedianMode()
    m.calculateMeanMedianMode (x)
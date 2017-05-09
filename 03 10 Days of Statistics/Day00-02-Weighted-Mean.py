'''
Objective
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

Input Format

The first line contains an integer, N, denoting the number of elements in arrays X and W.
The second line contains N space-separated integers describing the respective elements of array X.
The third line contains N space-separated integers describing the respective elements of array W.

Constraints
5<=N<=50
0<=X<i><=100, where x<i> is the ith element of array X.
0<=w<i><=100, where w<i> is the ith element of array W.

Output Format

Print the weighted mean on a new line. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).

Sample Input

5
10 40 30 50 20
1 2 3 4 5

Sample Output

32.0

Explanation

We use the following formula to calculate the weighted mean:
m<w>=(10*1+40*2+30*3+50*4+20*5)/(1+2+3+4+5)=480/15=32.0

And then print our result to a scale of decimal place () on a new line.
'''

class WeightedMean(object):
    def calculateWeightedMean (self, x,w):
        self.calculateWeightedMeanDef(x,w,1)

    def calculateWeightedMeanDef (self,x,w,d):
        for i in range(len(x)):
            x[i] = x[i] * w[i] / sum(w)
        print(round(sum(x),d))


if __name__ == '__main__':
    n = input().strip()
    n = int(n)
    x = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    w = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    m = WeightedMean()
    m.calculateWeightedMean (x,w)
'''
Objective
In this challenge, we practice using multiple linear regression. Check out the Tutorial tab for learning materials!

Task
Andrea has a simple equation:
        Y = a + b1*f1 + b2*f2 + ... + fm*xm
for (m+1) real constants (a, f1, f2, ..., fm). We can say that the value of Y depends on m features. Andrea studies this equation n for different feature sets (f1, f2, f3, ..., fm) and records each respective value of Y. If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?

Note: You are not expected to account for bias and variance trade-offs.

Input Format

The first line contains 2 space-separated integers, m(the number of observed features) and n(the number of feature sets Andrea studied), respectively.
Each of the n subsequent lines contain m+1 space-separated integers; the first m elements are features (f1, f2, f3, ..., fm), and the last element is the value of Y for the line's feature set.
The next line contains a single integer, q, denoting the number of feature sets Andrea wants to query for.
Each of the q subsequent lines contains m space-separated integers describing the feature sets.

Constraints
1<=m<=10
5<=n<=100
0<=x<i><=1
0<=Y<=10^6
1<=q<=100


Scoring
For each feature set in one test case, we will compute the following:

    . We will permit up to a margin of error.

The normalized score for each test case will be: . If the challenge is worth points, then your score will be .

Output Format

For each of the feature sets, print the value of on a new line (i.e., you must print a total of lines).

Sample Input

2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18

Sample Output

105.22
142.68
132.94
129.71

Explanation

We're given , so . We're also given , so we determine that Andrea studied the following feature sets:

We use the information above to find the values of , , and . Then, we find the value of for each of the feature sets.
'''

# Import library
from sklearn import linear_model

# Set data
m, n = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(n):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < m:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

# Get the parameters X for discovery the Y
q = int(input())
new_X = []
for i in range(q):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

# Gets the result and show on the screen
result = model.predict(new_X)
for i in range(len(result)):
    print(round(result[i],2))
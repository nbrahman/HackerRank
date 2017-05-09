'''
Objective
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

Input Format

A single line containing the following values:

1.09 1

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).
'''
import math

def BinomialPDF (x, n, p):
    return (math.factorial(n) * (p ** x) * ((1.0 - p) ** (n-x))) / (math.factorial(x) * math.factorial(n - x))

v = list(map(float, input().split()))
p = v[0] / (v[0] + v[1])
n = 6

print(round(BinomialPDF(3, n, p) + BinomialPDF(4, n, p) + BinomialPDF(5, n, p) + BinomialPDF(6, n, p), 3))

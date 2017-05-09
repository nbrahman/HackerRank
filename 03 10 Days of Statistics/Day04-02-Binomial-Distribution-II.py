'''
Objective
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

    No more than 2 rejects?
    At least 2 rejects?

Input Format

A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):

12 10

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print the answer to each question on its own line:

    The first line should contain the probability that a batch of 10 pistons will contain no more than 2 rejects.
    The second line should contain the probability that a batch of 10 pistons will contain at least 2 rejects.

Round both of your answers to a scale of 3 decimal places (i.e., 1.234 format).
'''
import math

def BinomialPDF (x, n, p):
    return (math.factorial(n) * (p ** x) * ((1.0 - p) ** (n-x))) / (math.factorial(x) * math.factorial(n - x))

v = list(map(float, input().split()))
p = v[0] / 100
n = int(v[1])

no_more_2_rejects = 0
for i in range(n):
    if i < 3:
        no_more_2_rejects = no_more_2_rejects + BinomialPDF(i, n, p)
print(round(no_more_2_rejects, 3))

at_least_2_rejects = 0
for i in range(n):
    if i > 1:
        at_least_2_rejects = at_least_2_rejects + BinomialPDF(i, n, p)
print(round(at_least_2_rejects, 3))

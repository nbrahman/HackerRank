'''
Objective
In this challenge, we go further with Poisson distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

    The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C<A> = 160 + 40x^2.
    The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C<B> = 128 + 40Y^2.

Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

Input Format

A single line comprised of 2 space-separated values denoting the respective means for A and B:

0.88 1.55

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e., 1.234 format):

    On the first line, print the expected daily cost of machine A.
    On the second line, print the expected daily cost of machine B.
'''

import math
def PoissonPDF(k, lam):
    return ((lam ** k) * (math.e ** (-1*lam))) / math.factorial(k)

meanA,meanB = list(map(float, input().strip().split(' ')))
costA = lambda a:160 + 40 * (a ** 2)
costB = lambda b:128 + 40 * (b ** 2)

print(round(sum([costA(a) * PoissonPDF(a, meanA) for a in range(0, 11)]), 3))
print(round(sum([costB(b) * PoissonPDF(b, meanB) for b in range(0, 11)]), 3))
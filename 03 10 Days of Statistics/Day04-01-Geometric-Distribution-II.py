'''
Objective
In this challenge, we go further with geometric distributions. We recommend reviewing the Geometric Distribution tutorial before attempting this challenge.

Task
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspections?

Input Format

The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of the first defect being discovered by:

1 3
5

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).
'''
prob = list(map(int, input().split()))
p = prob[0] / prob[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = 0
for i in range(n + 1):
    if i > 0:
        result += (q ** (i - 1) * p)

print(round(result, 3))
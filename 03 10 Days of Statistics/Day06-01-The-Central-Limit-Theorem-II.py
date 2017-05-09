'''
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem. We recommend reviewing the Central Limit Theorem Tutorial before attempting this challenge.

Task
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of mu=2.4 and a standard deviation of sigma=2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

Input Format

There are 4 lines of input (shown below):

250
100
2.4
2.0

The first line contains the number of last-minute tickets available at the box office. The second line contains the number of students waiting to buy tickets. The third line contains the mean number of purchased tickets, and the fourth line contains the standard deviation.

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print the probability that 100 students can successfully purchase the remaining 250 tickets, rounded to a scale of 4 decimal places (i.e., 1.2345 format).
'''

import math

def NormalPDF(stddev, mean, x):
    return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))

max_weight = float(input().strip())
no_of_boxes = float(input().strip())
mean = float(input().strip())
stddev = float(input().strip())

print(round(NormalPDF(stddev * (no_of_boxes ** 0.5), mean * no_of_boxes, max_weight), 4))
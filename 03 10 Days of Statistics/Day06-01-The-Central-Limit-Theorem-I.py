'''
Objective
In this challenge, we practice solving problems based on the Central Limit Theorem. Check out the Tutorial tab for learning materials!

Task
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean mu=205 of pounds and a standard deviation sigma=15 of pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

Input Format

There are 4 lines of input (shown below):

9800
49
205
15

The first line contains the maximum weight the elevator can transport. The second line contains the number of boxes in the cargo. The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation.

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print the probability that the elevator can successfully transport all 49 boxes, rounded to a scale of 4 decimal places (i.e., 1.2345 format).
'''

import math

def NormalPDF(stddev, mean, x):
    return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))

max_weight = float(input().strip())
no_of_boxes = float(input().strip())
mean = float(input().strip())
stddev = float(input().strip())

print(round(NormalPDF(stddev * (no_of_boxes ** 0.5), mean * no_of_boxes, max_weight), 4))
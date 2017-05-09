'''
Objective
In this challenge, we practice using linear regression techniques. Check out the Tutorial tab for learning materials!

Task
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of (x,y) points:
1. (95,85)
2. (85,95)
3. (80,70)
4. (70,65)
5. (60,70)

If a student scored 80 an on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x=80.

Input Format

There are five lines of input; each line contains two space-separated integers describing a student's respective x and y grades:

95 85
85 95
80 70
70 65
60 70

If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format

Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e., 1.234 format).
'''


# import library
import statistics as st

# Set data
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
meanX = st.mean(x)
meanY = st.mean(y)
x_s = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])

# Set the B and A
b = (n * xy - sum(x) * sum(y)) / (n * x_s - (sum(x) ** 2))
a = meanY - b * meanX

# Gets the result and show on the screen
print (round(a + 80 * b, 3))
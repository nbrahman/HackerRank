'''
Colleen is turning n years old! She has n candles of various heights on her
cake, and candle i has height height[i]. Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given the height[i] for each individual candle, find and print the number of
candles she can successfully blow out.

Input Format

The first line contains a single integer, , denoting the number of candles on the cake.
The second line contains space-separated integers, where each integer describes the height of candle .

Constraints
1<=n<=10^5
1<=height[i]<=10^7

Output Format

Print the number of candles Colleen blows out on a new line.

Sample Input 0

4
3 2 1 3

Sample Output 0

2

Explanation 0

We have one candle of height 1, one candle of height 2, and two candles of
height 3. Colleen only blows out the tallest candles, meaning the candles where height=3. Because there are 2 such candles, we print 2 on a new line.
'''

#!/bin/python3

import sys

height = []
n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
print (height.count(max(height)))
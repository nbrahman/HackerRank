'''
Consider a bijective function f: X -> Y.

Define another function g: Y -> X so that for and if then .

Now, the function is said to be the inverse function of and is denoted as .

In this task, you'll be given an integer and a bijective function where .

Output the inverse of .

Input Format

There are lines in the input.
The first line contains a single positive integer .
The second line contains space separated integers, the values of , respectively.

Constraints

Output Format

Output lines. The line should contain the value of .

Sample Input#00

3
1 2 3

Sample Output#00

1
2
3

Sample Input#01

3
2 3 1

Sample Output#01

3
1
2

Explanation

First sample :-

Basically, this is the function . Hence, it's the inverse of itself.

Second Sample :-

Here you can see that

hence is
is
is

One way to confirm is . 
'''
n = int(input().strip())
l = list(map(int, input().strip().split(' ')))
p = []
for i in range(1, n+1):
    p.append(i)
z = zip (l, p)
z = sorted (z, key=lambda x:x[0])
for i in z:
    print(i[1])
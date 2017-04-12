'''
Consider a 3 X 3 matrix, s, of integers in the inclusive range [1,9]. Any digit, a, can be changed to any other digit, b, in the range [1,9] at cost |a-b|.

Given matrix s, convert it into a magic square by changing zero, one, or more of the digits in s. You must do this in such a way that the cost is minimal and then print the minimum possible cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].

Input Format

There are 3 lines of input. Each line describes a row of the matrix in the form of 3 space-separated integers denoting the respective first, second, and third elements of that row.

Constraints

    All integers in s are in the inclusive range [1,9].

Output Format

Print a single integer denoting the smallest possible cost of turning matrix s into a magic square.

Sample Input

4 9 2
3 5 7
8 1 5

Sample Output

1

Explanation

Matrix s initially looks like this:

4 9 2
3 5 7
8 1 5

Observe that it's not yet magic, because not all rows, columns, and center diagonals sum to the same number.

If we change the bottom right value, s[2][2], from 5 to 6 at a cost of |6-5|=1, s will become a magic square at the minimum possible cost. Thus, we print the cost, 1, on a new line.
'''
def msf(perm,matrix,mincost):
    for itm in perm:
        curr = 0
        for i in range(3):
            for j in range(3):
                curr += abs(matrix[i][j] - itm[i][j])
        mincost = min(curr, mincost)
    print (mincost)


perm = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

matrix = []

for i in range(3):
    matrix.append(list(map(int, input().strip().split(' '))))

mincost = 81
msf(perm,matrix,mincost)
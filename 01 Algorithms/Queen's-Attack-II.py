'''
A queen is standing on an  n x n chessboard. The chessboard's rows are numbered from 1 to n, going from bottom to top; its columns are numbered from 1 to n, going from left to right. Each square on the board is denoted by a tuple, (r,c), describing the row, r, and column, c, where the square is located.

The queen is standing at position (r<q>,c<q>) and, in a single move, she can attack any square in any of the eight directions (left, right, up, down, or the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from (4,4):

image

There are k obstacles on the chessboard preventing the queen from attacking any square that has an obstacle blocking the the queen's path to it. For example, an obstacle at location (3,5) in the diagram above would prevent the queen from attacking cells (3,5), (2,6), and (1,7):

image

Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at (r<q>,c<q>).

Input Format

The first line contains two space-separated integers describing the respective values of n(the side length of the board) and k(the number of obstacles).
The next line contains two space-separated integers describing the respective values of r<q> and c<q>, denoting the position of the queen.
Each line i of the k subsequent lines contains two space-separated integers describing the respective values of r<i> and c<i>, denoting the position of obstacle .

Constraints
0<=n,k<=10^5
A single cell may contain more than one obstacle; however, it is guaranteed that there will never be an obstacle at position (r<q>,c<q>) where the queen is located.

Subtasks

For 30% of the maximum score:
0<=n,k<=100

For 55% of the maximum score:
0<=n<=1000
0<=k<=10^5

Output Format

Print the number of squares that the queen can attack from position (r<q>,c<q>).

Sample Input 0

4 0
4 4

Sample Output 0

9

Explanation 0

The queen is standing at position (4,4) on a 4 x 4 chessboard with no obstacles:

image

We then print the number of squares she can attack from that position, which is 9.

Sample Input 1

5 3
4 3
5 5
4 2
2 3

Sample Output 1

10

Explanation 1

The queen is standing at position (4,3) on a 5 x 5  chessboard with k=3 obstacles:

image

We then print the number of squares she can attack from that position, which is 10.
'''

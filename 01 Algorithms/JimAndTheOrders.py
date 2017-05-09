'''
Jim's Burgers has n hungry burger fans waiting in line. Each unique order, i, is placed by a customer at time ti, and the order takes di units of time to process.

Given the information for all n orders, can you find and print the order in
which all n customers will receive their burgers? If two or more orders are fulfilled at the exact same time t, sort them by ascending order number.

Input Format

The first line contains a single integer, , denoting the number of orders.
Each of the subsequent lines contains two space-separated integers describing the respective values of and for order .

Constraints
1 <= n <= 10^3
1 <= i <= n
1 <= ti,di <= 10^6

Output Format

Print a single line of n space-separated order numbers (recall that orders are numbered from 1 to n) describing the sequence in which the customers receive their burgers. If two or more customers receive their burgers at the same time, print the smallest order number first.

Sample Input 0

3
1 3
2 3
3 3

Sample Output 0

1 2 3

Explanation 0

Jim has the following orders:

1. t1=1, d1=3. This order is fulfilled at time t = 1 + 3 = 4.
2. t2=2, d2=3. This order is fulfilled at time t = 2 + 3 = 5.
3. t3=3, d3=3. This order is fulfilled at time t = 3 + 3 = 6.

As you can see, order 1 was fulfilled at time t=4, order 2 was fulfilled at
time 5, and order 3 was fulfilled at time 6. Thus, we print the sequence of order numbers in the order in which they were fulfilled as 1 2 3.

Sample Input 1

5
8 1
4 2
5 6
3 1
4 3

Sample Output 1

4 2 5 1 3

Explanation 1

Jim has the following orders:

1. t1=8, d1=1. This order is fulfilled at time t = 8 + 1 = 9.
2. t2=4, d2=2. This order is fulfilled at time t = 4 + 2 = 6.
3. t3=5, d3=6. This order is fulfilled at time t = 5 + 6 = 11.
4. t4=3, d4=1. This order is fulfilled at time t = 3 + 1 = 4.
5. t5=4, d5=3. This order is fulfilled at time t = 4 + 3 = 7.

When we order these by ascending fulfillment time, we get:

t=4  : order 4.
t=6  : order 2.
t=7  : order 5.
t=9  : order 1.
t=11 : order 3.


We print the ordered numbers in the bulleted listed above as 4 2 5 1 3.

Note: While not demonstrated in these sample cases, recall that any orders fulfilled at the same time must be listed by ascending order number.
'''
if __name__ == '__main__':
    n = int(input().strip())

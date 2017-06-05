#!/bin/python3

import sys


def make_change(coins, n, m):
    table = [0 for k in range(n + 1)]

    table[0] = 1

    for i in range(0, m):
        for j in range(coins[i], n + 1):
            table[j] += table[j - coins[i]]

    return table[n]


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n, m))

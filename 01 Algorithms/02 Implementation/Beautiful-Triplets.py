import sys


x = list(map(int,input().strip().split(' ')))
n=x[0]
d=x[1]
a = list(map(int,input().strip().split(' ')))

cnt = 0
for i in range(n):
    if a[i] + d in a and a[i] + 2 * d in a:
        cnt += 1
print(cnt)
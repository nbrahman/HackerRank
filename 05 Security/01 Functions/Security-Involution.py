n = int(input().strip())
l = list(map(int, input().strip().split(' ')))
flg = True
i = 0
while i < n and flg:
    if l[l[i]-1] != (i + 1):
        flg = False
    i += 1
if flg:
    print('YES')
else:
    print('NO')
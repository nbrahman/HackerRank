t1, t2, n = map(int, input().strip().split(' '))
for i in range(2, n):
    t = t1 + (t2 ** 2)
    t1 = t2
    t2 = t
    print (t1, t2, t)
print(t)
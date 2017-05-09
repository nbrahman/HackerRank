s = input().strip()
sum = 0
mod = 1000000007
p = 1
n = len(s)
ps = [0] * 200007
for i in range (n):
    ps[i] = (ps[i - 1] + int(s[i]) * (i + 1)) % mod

for i in range(n):
    sum = (sum + ps[n - i - 1] * p) % mod
    p = (p * 10) % mod
print(sum)
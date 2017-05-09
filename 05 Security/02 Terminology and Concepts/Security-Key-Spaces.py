import sys

def ciphertext2(s, k):
    res = ''
    for i in s:
        res += str((int(i) + k) % 10)
    return res


n = input().strip()
k = int(input().strip())
print(ciphertext2(n, k))
import sys

def ciphertext(s):
    res = ''
    for i in s:
        res += str((int(i) + 1) % 10)
    return res


n = input().strip()
print(ciphertext(n))
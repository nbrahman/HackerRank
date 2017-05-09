from collections import Counter

def number_needed(a, b):
    c_a = Counter(a)
    c_b = Counter(b)
    cnt = 0
    s = set(c_a.keys()).union(c_b.keys())
    for k in s:
        cnt += max (c_a.get(k, 0)-c_b.get(k, 0), c_b.get(k, 0)-c_a.get(k, 0))
    return cnt





a = input().strip()
b = input().strip()

print(number_needed(a, b))

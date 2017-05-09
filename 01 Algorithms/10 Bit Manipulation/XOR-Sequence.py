def xol(l, r):
    odd = (r - l) % 2 == 0

    if odd:
        base = xor_sum(l)
        res = base ^ (xor_sum(l, True) ^ xor_sum(r, True))
    else:
        base = 0
        res = base ^ (xor_sum(l - 1, True) ^ xor_sum(r, True))

    return res


def xor_sum(i, two_steps=False):
    m = 2 if two_steps else 1
    if i % 2 != 0:
        offset = ((1 + i) / m) % 4
    else:
        offset = (1 + (i / m)) % 4
    sum_ = [0,
            0 ^ i,
            0 ^ (i - 1 * m) ^ i,
            0 ^ (i - 2 * m) ^ (i - 1 * m) ^ i]
    assert offset % 1 == 0
    return sum_[int(offset)]


q = int(input().strip())
for i in range(q):
    l, r = map(int, input().strip().split(' '))
    print(xol(l, r))
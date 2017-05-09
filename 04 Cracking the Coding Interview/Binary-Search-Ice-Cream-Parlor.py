def BinarySearch (cnt, pos, price):
    rightIndex = len(cnt) - 1
    leftIndex = pos + 1
    while leftIndex <= rightIndex:
        midIndex = (leftIndex + rightIndex) // 2
        if cnt[midIndex][0] == price:
            return cnt[midIndex][1]

        if cnt[midIndex][0] > price:
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1

def CallBinarySearch(m, p):
    cnt = sorted([(price, f + 1) for f, price in enumerate (p)])
    for i in range(len(cnt)):
        srch = BinarySearch(cnt, i, m - cnt[i][0])
        if srch:
            ret = sorted([cnt[i][1], srch])
            return '{} {}'.format(*ret)



t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print (CallBinarySearch(m, a))

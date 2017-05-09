n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
totSwaps = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            totSwaps += 1
print('Array is sorted in',totSwaps,'swaps.')
print('First Element:', a[0])
print('Last Element:',a[len(a)-1])
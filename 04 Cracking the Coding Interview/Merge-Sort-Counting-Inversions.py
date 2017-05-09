def mergeSort(a):
    if len(a)>1:
        [a1, a2] = divide(a)
        a1, invLeft = mergeSort(a1)
        a2, invRight = mergeSort(a2)
        final, invSplit = merge (a1, a2)
        return final, invLeft + invRight + invSplit
    else:
        return a, 0

def divide(a):
    return [a[:int(len(a)/2)], a[int(len(a)/2):]]

def merge(a1, a2):
    a = []
    posA1 = 0
    posA2 = 0
    invCnt = 0
    lenA1 = len(a1)
    lenA2 = len(a2)
    while posA1 < lenA1 and posA2 < lenA2:
        if a1[posA1] <= a2[posA2]:
            a.append(a1[posA1])
            posA1 += 1
        else:
            a.append(a2[posA2])
            posA2 += 1
            invCnt += (lenA1 - posA1)

    for i in range (posA1, lenA1):
        a.append(a1[i])

    for i in range (posA2, lenA2):
        a.append(a2[i])

    return a, invCnt


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    arr, invCnt = mergeSort(arr)
    print(invCnt)

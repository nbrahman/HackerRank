def isModKaprekar(p, q):
    cnt = 0
    for n in range(p, q+1):
        if n == 1:
            print(n,end=' ')
            cnt += 1
        strSqr = str(n ** 2)
        l = len(strSqr)
        if l <= 1:
            pass
        else:
            temp = int(strSqr[0:int(l/2)]) + int(strSqr[int(l/2):])
            if temp == n:
                print(n, end=' ')
                cnt += 1
            else:
                pass

    if cnt == 0:
        print('INVALID RANGE')

p = int(input().strip())
q = int(input().strip())
isModKaprekar(p, q)
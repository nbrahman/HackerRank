from math import sqrt
def isPrime(n):
    if n < 2:
        return 'Not prime'
    elif n == 2:
        return 'Prime'
    elif n % 2 == 0:
        return 'Not prime'
    else:
        for i in range(3, int(sqrt(n)+1),2):
            if (n % i == 0):
                return 'Not prime'
    return 'Prime'

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    print(isPrime(n))

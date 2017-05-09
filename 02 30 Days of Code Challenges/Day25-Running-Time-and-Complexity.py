import math

def isPrime(n):
    if n < 2:
        return 'Not prime'
    elif n == 2:
        return 'Prime'
    elif n % 2 == 0:
        return 'Not prime'
    else:
        for i in range(3, int(math.sqrt(n)+1),2):
            if (n % i == 0):
                return 'Not Prime'
    return 'Prime'


t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(isPrime(n))
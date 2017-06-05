# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#     #return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

mem = {}
def fibonacci(n):
    if n < 3:
        return n
    elif n == 3:
        return 4
    try:
        return mem[n]
    except:
        mem[n] = fibonacci(n - 1) + fibonacci(n - 2) + fibonacci(n - 3)
        return mem[n]

n = int(input())
for i in range (n):
    p = int(input())
    print(fibonacci(p))

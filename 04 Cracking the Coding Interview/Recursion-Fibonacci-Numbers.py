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
    if n < 2:
        return n
    try:
        return mem[n]
    except:
        mem[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return mem[n]

n = int(input())
print(fibonacci(n))

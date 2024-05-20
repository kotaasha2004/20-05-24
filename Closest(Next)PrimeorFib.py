import math
def isPrime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=count+1
    if count==0:
        return True
def isPerfect(n):
    s=int(math.sqrt(n))
    return s*s==n
def isFibbno(n):
    return  isPerfect(5*n*n+4) or isPerfect(5*n*n-4)
def find_next_fib_or_prime(n):
    while True:
        if isPrime(n) or isFibbno(n):
            print(n)
            break
        n=n+1
num=int(input())
if num<100000:
    find_next_fib_or_prime(num)

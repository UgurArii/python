from functools import reduce
nums = [1,2,3,4]
result =reduce(lambda a,b:a*b,nums)
print(result)

#facktoriyel

def factorial(n):
    #seet your base case
    if n <=1:
        return 1
    else:
        return factorial(n-1) * n
print(factorial(5))

#fibonacci
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))
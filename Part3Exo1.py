def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print(fact(5))

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))

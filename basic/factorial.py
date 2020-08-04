def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


assert factorial(5) == 120
assert factorial(1) == 1
assert factorial(4) == 24
assert factorial(10) == 3628800

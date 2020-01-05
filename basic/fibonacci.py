# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025
def fibonacci_series(num):
    f, s = 0, 1
    while f < num:
        print(f, end=' ')
        f, s = s, f + s


# fibonacci_series(5)


def fibonacci_recu(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recu(n - 1) + fibonacci_recu(n - 2)


print(fibonacci_recu(8))

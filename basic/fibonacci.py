# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025
def fibonacci_loop(num):
    f, s = 0, 1
    while f < num:
        print(f, end=' ')
        f, s = s, f + s


fibonacci_loop(100000)

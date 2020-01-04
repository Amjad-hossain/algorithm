def gcd(f, s):
    while s > 0:
        f, s = s, f % s
    return f


print(gcd(6, 4))
print(gcd(4, 6))
print(gcd(2, 3))
print(gcd(3, 2))
print(gcd(9, 27))
print(gcd(27, 9))


def lcm_recu(f, s):
    return (s * f) // gcd(f, s)


print(lcm_recu(6, 4))
print(lcm_recu(4, 6))
print(lcm_recu(2, 3))
print(lcm_recu(3, 2))
print(lcm_recu(9, 27))
print(lcm_recu(27, 9))


def lcm_loop(f, s):
    d = 2
    m = 1
    while f > 1 and s > 1:
        if f % d != 0 and s % d != 0:
            d = d + 1
            continue
        if f % d == 0:
            f //= d
        if s % d == 0:
            s //= d
        m = m * d
    return m * f * s


print(lcm_loop(6, 4))
print(lcm_loop(4, 6))
print(lcm_loop(2, 3))
print(lcm_loop(3, 2))
print(lcm_loop(9, 27))
print(lcm_loop(27, 9))

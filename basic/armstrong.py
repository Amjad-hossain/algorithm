def armstrong(num, total):
    if num == 0:
        return total

    digit = num % 10
    total += digit ** 3
    return armstrong(num // 10, total)


num = 153

print('Is {} armstrong number?'.format(num), num == armstrong(num, 0))


def find_armstrong_number(start, max):
    for num in range(start, max + 1):
        if num == armstrong(num, 0):
            print('{} is armstrong'.format(num))


find_armstrong_number(1, 5000)

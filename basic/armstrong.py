# Armstrong number:
#
# A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
#
# For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

def armstrong(num, total):
    if num == 0:
        return total

    digit = num % 10
    total += digit * digit * digit
    return armstrong(num // 10, total)


num = 153
print(num == armstrong(num, 0))

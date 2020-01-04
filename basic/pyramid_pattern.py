# *
# * *
# * * *
# * * * *
# * * * * *

def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_star in range(current_row + 1):
            print('* ', end='')
        print()


pyramid(5)
print('---------')


# * * * * *
# * * * *
# * * *
# * *
# *

def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_star in range(max_row - current_row):
            print('* ', end='')
        print()


pyramid(5)
print('---------')


#     *
#    **
#   ***
#  ****
# *****

def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_space in range(max_row - current_row - 1):
            print(' ', end='')
        for number_of_start in range(current_row + 1):
            print('*', end='')

        print()


pyramid(5)
print('---------')


#     *
#    * *
#   * * *
#  * * * *
# * * * * *

def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_space in range(max_row - current_row - 1):
            print(' ', end='')
        for number_of_start in range(current_row + 1):
            print('* ', end='')

        print()


pyramid(5)
print('---------')


# *****
#  ****
#   ***
#    **
#     *

def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_space in range(current_row):
            print(' ', end='')
        for number_of_start in range(max_row - current_row):
            print('*', end='')

        print()


pyramid(5)
print('---------')


# * * * * *
#  * * * *
#   * * *
#    * *
#     *
def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_space in range(current_row):
            print(' ', end='')
        for number_of_star in range(max_row - current_row):
            print('* ', end='')

        print()


pyramid(5)
print('---------')


# 1 2 3 4 5
#  2 3 4 5
#   3 4 5
#    4 5
#     5


def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_space in range(current_row):
            print(' ', end='')
        for number in range(max_row - current_row):
            print(number + current_row + 1, end=' ')

        print()


pyramid(5)
print('---------')


# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1


def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_space in range(current_row):
            print(' ', end='')
        for number in range(max_row - current_row):
            print(number + 1, end=' ')

        print()


pyramid(5)

print('---------')


#     A
#    A B
#   A B C
#  A B C D
# A B C D E

def pyramid(max_row):
    for current_row in range(max_row):
        for number_of_space in range(max_row - current_row - 1):
            print(' ', end='')
        for col in range(current_row + 1):
            print(chr(col + 65), end=' ')

        print()


pyramid(5)

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

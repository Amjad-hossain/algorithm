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

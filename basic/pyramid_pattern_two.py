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

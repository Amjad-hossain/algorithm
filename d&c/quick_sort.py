# The algorithm picks a pivot element, rearranges the array elements in such a way that all elements smaller
# than the picked pivot element move to left side of pivot,
# and all greater elements move to right side.
# Finally, the algorithm recursively sorts the sub-arrays on left and right of pivot element.

def quick_sort(dataset, first, last):
    if first < last:
        pivot_index = partition(dataset, first, last)
        quick_sort(dataset, first, pivot_index - 1)
        quick_sort(dataset, pivot_index + 1, last)


def partition(dataset, first, last):
    # Choose the first item
    pivotvalue = dataset[first]
    # establish upper and lower indexes

    lower = first + 1
    upper = last

    # Start searching for crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and dataset[lower] <= pivotvalue:
            lower += 1
        # decrease the upper index
        while lower <= upper and pivotvalue <= dataset[upper]:
            upper -= 1

        # If the two indexws crossed, we got the split point
        if upper < lower:
            done = True
        else:
            # Exchange the values
            temp = dataset[lower]
            dataset[lower] = dataset[upper]
            dataset[upper] = temp

    # Exchange the pivot value
    dataset[first] = dataset[upper]
    dataset[upper] = pivotvalue

    # return split index
    return upper


a = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
quick_sort(a, 0, len(a) - 1)
print(a)

a = [9, 8, 7, 6, 5, 4]
quick_sort(a, 0, len(a) - 1)
print(a)

a = [5, 6, 7, 8, 9, 2]
quick_sort(a, 0, len(a) - 1)
print(a)

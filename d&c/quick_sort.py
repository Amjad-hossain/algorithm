# The algorithm picks a pivot element, rearranges the array elements in such a way that all elements smaller
# than the picked pivot element move to left side of pivot,
# and all greater elements move to right side.
# Finally, the algorithm recursively sorts the sub-arrays on left and right of pivot element.

def quick_soft(a):
    l = 0
    al = len(a) - 1
    r = al
    while l < al:
        while l < r:
            if a[r - 1] > a[r]:
                a[r - 1], a[r] = a[r], a[r - 1]
            r = r - 1
        r = al
        l = l + 1
    return a


a = [7, 2, 9, 3, 4, 5]
print(quick_soft(a))

a = [9, 2, 9, 3, 2, 8]
print(quick_soft(a))

a = [9, 8, 7, 6, 5, 4]
print(quick_soft(a))
a = [5, 6, 7, 8, 9, 2]
print(quick_soft(a))

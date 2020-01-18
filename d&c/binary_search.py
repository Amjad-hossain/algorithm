# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

def binary_search(a, k):
    l = 0
    r = len(a) - 1

    while l <= r:
        m = (l + r) // 2
        if a[m] == k:
            return m
        elif a[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert binary_search(a, 4) == 4
assert binary_search(a, 2) == 2
assert binary_search(a, 7) == 7
assert binary_search(a, 9) == 9
assert binary_search(a, 0) == 0
assert binary_search(a, 11) == -1
assert binary_search(a, -1) == -1

a = [2, 3, 5, 6, 7, 9]
assert binary_search(a, 7) == 4

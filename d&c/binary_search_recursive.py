# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

def binary_search_recursive(a, k, l, r):
    if l > r:
        return -1
    m = (l + r) // 2
    if a[m] == k:
        return m
    elif a[m] > k:
        return binary_search_recursive(a, k, l, m - 1)
    else:
        return binary_search_recursive(a, k, m + 1, r)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert binary_search_recursive(a, 4, 0, 9) == 4
assert binary_search_recursive(a, 2, 0, 9) == 2
assert binary_search_recursive(a, 7, 0, 9) == 7
assert binary_search_recursive(a, 9, 0, 9) == 9
assert binary_search_recursive(a, 0, 0, 9) == 0
assert binary_search_recursive(a, 11, 0, 9) == -1
assert binary_search_recursive(a, -1, 0, 9) == -1

a = [2, 3, 5, 6, 7, 9]
assert binary_search_recursive(a, 7, 0, 5) == 4

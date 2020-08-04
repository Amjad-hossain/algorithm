# The algorithm picks a pivot element, rearranges the array elements in such a way that all elements smaller
# than the picked pivot element move to left side of pivot,
# and all greater elements move to right side.
# Finally, the algorithm recursively sorts the sub-arrays on left and right of pivot element.


def merge_sort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftdata = dataset[:mid]
        rightdata = dataset[mid:]

        # Recursively break the dataset
        merge_sort(leftdata)
        merge_sort(rightdata)

        index_lf = 0
        index_rd = 0
        index_md = 0

        # While both arrays have content
        while index_lf < len(leftdata) and index_rd < len(rightdata):
            if leftdata[index_lf] < rightdata[index_rd]:
                dataset[index_md] = leftdata[index_lf]
                index_lf += 1
            else:
                dataset[index_md] = rightdata[index_rd]
                index_rd += 1
            index_md += 1

        # If the leftdata still has values, add them
        while index_lf < len(leftdata):
            dataset[index_md] = leftdata[index_lf]
            index_lf += 1
            index_md += 1

        # If the rightdata still has values, add them
        while index_rd < len(rightdata):
            dataset[index_md] = rightdata[index_rd]
            index_rd += 1
            index_md += 1

        # return dataset


a = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
merge_sort(a)
print(a)

""" Merge Sort
The Merge Sort is a recursive sort of order n*log(n).

It is notable for having a worst case and average complexity of O(n*log(n)),
and a best case complexity of O(n) (for pre-sorted input).

The basic idea is to split the collection into smaller groups by halving it
until the groups only have one element or no elements (which are both entirely
sorted groups).Then merge the groups back together so that their elements are
in order.

This is how the algorithm gets its "divide and conquer" description.
"""


def merge(left, right):
    """Merge two list keeping the elements in order."""
    if len(left) * len(right) == 0:
        return left + right

    merge_list = (left[0] < right[0] and left or right).pop(0)
    return [merge_list] + merge(left, right)


def mergesort(unsorted_list):
    """Merge Sort function."""
    if len(unsorted_list) < 2:
        return unsorted_list

    mid = len(unsorted_list) / 2
    left_part = mergesort(unsorted_list[:int(mid)])
    right_part = mergesort(unsorted_list[int(mid):])
    return merge(left_part, right_part)

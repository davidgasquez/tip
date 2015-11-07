"""Merge Sort Algorithm.

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
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.

    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """

    # Check if any list is empty
    if len(left) * len(right) == 0:
        return left + right

    # Merge keeping the order
    merge_list = (left[0] < right[0] and left or right).pop(0)

    return [merge_list] + merge(left, right)


def mergesort(unsorted_list):
    """Sorts the input list using the merge sort algorithm.

    >>> lst = [4, 5, 1, 6, 3]
    >>> merge_sort(lst)
    [1, 3, 4, 5, 6]
    """
    # Lists of 1 elements are already sorted
    if len(unsorted_list) < 2:
        return unsorted_list

    # Set the split point
    mid = len(unsorted_list) / 2

    # Divide
    left_part = mergesort(unsorted_list[:int(mid)])
    right_part = mergesort(unsorted_list[int(mid):])

    return merge(left_part, right_part)

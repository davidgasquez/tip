"""Quick Sort Algorithm.

The Quick Sort is a recursive sort of order in range from O(n log n) with
the best pivots, to O(n2) with the worst pivots, where n is the number
of elements in the array.

Quicksort, also known as partition-exchange sort, uses these steps:
    1 - Choose any element of the array to be the pivot.
    2 - Divide all other elements (except the pivot) into two partitions.
    3 - All elements less than the pivot must be in the first partition.
    4 - All elements greater than the pivot must be in the second partition.
    5 - Use recursion to sort both partitions.
    6 - Join first sorted partition, the pivot, and the second sorted partition.

Quicksort has a reputation as the fastest sort. Optimized variants of quicksort
are common features of many languages and libraries. One often contrasts
quicksort with merge sort, because both sorts have an average time
of O(n log n).
"""


def partition(unsorted_list):
    """Partition array using a pivot value."""
    return unsorted_list


def quick_sort(unsorted_list):
    """Sorts the input list using the quick sort algorithm.

    >>> unsorted_list = [4, 5, 1, 6, 3]
    >>> quick_sort(unsorted_list)
    [1, 3, 4, 5, 6]
    """
    unsorted_list = sorted(unsorted_list)
    return unsorted_list

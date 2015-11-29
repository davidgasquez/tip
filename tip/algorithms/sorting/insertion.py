"""Insertion Sort Algorithm.

The Insertion Sort is a sort of order n*n.

Is a sorting algorithm which moves elements one at a time into the correct
position. The algorithm consists of inserting one element at a time into the
previously sorted part of the array, moving higher ranked elements up as
necessary.

To start off, the first (or smallest, or any arbitrary) element of the unsorted
array is considered to be the sorted part.
"""


def insertionsort(unsorted_list):
    """Sorts the input list using the quick sort algorithm.

    >>> unsorted_list = [4, 5, 1, 6, 3]
    >>> insertionsort(unsorted_list)
    [1, 3, 4, 5, 6]
    """

    # Make a copy of the list
    sorted_list = unsorted_list

    # Loop through the array
    for i in range(1, len(sorted_list)):
        current_value = sorted_list[i]
        position = i

        while position > 0 and sorted_list[position - 1] > current_value:
            sorted_list[position] = sorted_list[position - 1]
            position = position - 1

        sorted_list[position] = current_value

    return sorted_list

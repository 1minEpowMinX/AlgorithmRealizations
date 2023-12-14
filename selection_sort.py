def find_smallest(array: list) -> int:
    """
(GENERAL!) Realization of selection sort algorithm. In this case sort by integers.
Computing complexity: O(n^2).

Args:
    array (list): unsorted list of integers

Returns:
    int: minimum index of array elements
    """
    min_el = array[0]
    min_ind = 0
    for i in range(1, len(array)):
        if array[i] < min_el:
            min_el = array[i]
            min_ind = i

    return min_ind


def selectionSort(array: list) -> list:
    """
(GENERAL!) Realization of selection sort algorithm. In this case sort by integers.
Computing complexity: O(n^2).

Args:
    array (list): unsorted list of integers

Returns:
    list: list of integers sorted by escanding 
    """
    newArray = []
    for i in array:
        minimum = find_smallest(array)
        newArray.append(minimum)

    return newArray

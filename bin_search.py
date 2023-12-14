from typing import Any


def binary_search(arr: list, item: Any) -> Any:
    '''
    !GENERAL! Realization of binary search in Python.
    Computing complexity: O(log n)
    :param: arr
    :type arr: list
    :param: item
    :type: Any
    :return: item type, if the item is in arr, or None otherwise
    :rtype: item type, if the item is in arr, or None otherwise
    '''
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            return guess
    return None

help(binary_search)
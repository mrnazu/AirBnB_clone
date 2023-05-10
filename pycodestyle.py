def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found, return the index
        elif mid_value < target:
            low = mid + 1  # Target is in the right half, update low to mid + 1
        else:
            high = mid - 1  # Target is in the left half, update high to mid - 1

    return -1  # Target not found, return -1



"""
The code uses a while loop to iterate over the elements of an array using the binary search algorithm to find a specific element. The binary search algorithm always runs in O(log n) time, which means that the number of comparisons made by the algorithm is proportional to the logarithm of the size of the array, assuming the target element is present in the array.

The function returns the index of the target element if it's found, otherwise it returns -1 to indicate that the target element was not found in the array. The function is named binary_search to indicate that it implements a binary search algorithm, and it takes the array and target element as inputs.
"""

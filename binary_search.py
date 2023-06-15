def binary_search(arr, find):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == find:
            return True
        if arr[middle] > find:
            right = middle - 1
        else:
            left = middle + 1
    return False

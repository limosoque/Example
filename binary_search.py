def binary_search(arr: list, find:int):
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


# arr_size, find_count = [x for x in input().split()]
# arr = [int(x) for x in input().split()]
# find = [int(x) for x in input().split()]
#
# for to_find in find:
#     print(binary_search(arr, to_find))

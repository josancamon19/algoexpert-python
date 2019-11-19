def shiftedBinarySearch(array, target):
    # Write your code here.
    pivot = find_pivot(array, 0, len(array) - 1)
    if target == array[pivot]:
        return pivot
    elif target < array[0]:
        array = array[pivot + 1:]
        idx = binary_search(array, 0, len(array) - 1, target)
        if idx != -1:
            idx += pivot + 1
        return idx
    array = array[: pivot]
    return binary_search(array, 0, len(array) - 1, target)


def find_pivot(array, left_idx, right_idx):
    mid_idx = (left_idx + right_idx) // 2
    mid = array[mid_idx]

    if mid_idx + 1 >= len(array):
        return -1

    if array[mid_idx + 1] < mid:
        return mid_idx
    elif array[mid_idx - 1] > mid:
        return mid_idx - 1
    elif array[left_idx] > mid:
        return find_pivot(array, left_idx, mid_idx - 1)
    return find_pivot(array, mid_idx + 1, right_idx)


def binary_search(array, left_idx, right_idx, target):
    if left_idx > right_idx:
        return -1

    mid_idx = (left_idx + right_idx) // 2
    mid = array[mid_idx]

    if mid == target:
        return mid_idx
    elif mid < target:
        return binary_search(array, mid_idx + 1, right_idx, target)
    return binary_search(array, left_idx, mid_idx - 1, target)


if __name__ == '__main__':
    # print(shiftedBinarySearch([1, 2, 3], 4))
    print(shiftedBinarySearch([73, 0, 1, 21, 33, 45, 45, 61, 71, 72], 70))

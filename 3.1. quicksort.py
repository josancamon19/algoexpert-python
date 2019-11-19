# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     def sort(array, pivot_idx, right_idx):
#         left_idx = pivot_idx + 1
#         while right_idx >= left_idx:
#             pivot = array[pivot_idx]
#             left = array[left_idx]
#             right = array[right_idx]
#
#             if left > pivot > right:
#                 swap(array, left_idx, right_idx)
#             if left <= pivot:
#                 left_idx += 1
#             if right >= pivot:
#                 right_idx -= 1
#
#             # print(left_idx, right_idx, array)
#         swap(array, pivot_idx, right_idx)
#         # print(array)
#         # now right idx is ok lets do the same for array[:right_idx] and array[right_idx + 1:]
#         return quickSort(array[:right_idx]) + [array[right_idx]] + quickSort(array[right_idx + 1:])
#
#     # print('------')
#     return sort(arr, 0, len(arr) - 1)

def quickSort(arr):
    sort_last_as_pivot(arr, 0, len(arr) - 1)
    return arr


def sort_first_as_pivot(array, start_idx, end_idx):  # sort using the first index as pivot
    if start_idx >= end_idx:
        return

    pivot_idx = start_idx
    left_idx = pivot_idx + 1
    right_idx = end_idx

    while right_idx >= left_idx:
        pivot = array[pivot_idx]
        left = array[left_idx]
        right = array[right_idx]

        if left > pivot > right:
            swap(array, left_idx, right_idx)
        if left <= pivot:
            left_idx += 1
        if right >= pivot:
            right_idx -= 1

    swap(array, pivot_idx, right_idx)

    # print(pivot_idx, start_idx, left_idx, right_idx, end_idx)
    left_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)
    if left_smaller:
        sort_first_as_pivot(array, start_idx, right_idx - 1)
        sort_first_as_pivot(array, right_idx + 1, end_idx)
    else:
        sort_first_as_pivot(array, right_idx + 1, end_idx)
        sort_first_as_pivot(array, start_idx, right_idx - 1)


def sort_last_as_pivot(array, start_idx, end_idx):  # sort using the last index as pivot
    if start_idx >= end_idx:
        return

    pivot_idx = end_idx
    left_idx = start_idx
    right_idx = pivot_idx - 1

    while right_idx >= left_idx:
        pivot = array[pivot_idx]
        left = array[left_idx]
        right = array[right_idx]

        if left > pivot > right:
            swap(array, left_idx, right_idx)
        if left <= pivot:
            left_idx += 1
        if right >= pivot:
            right_idx -= 1

    swap(array, pivot_idx, left_idx)

    # print(array)

    left_smaller = right_idx - 1 - start_idx < end_idx - (right_idx + 1)
    if left_smaller:
        sort_last_as_pivot(array, start_idx, left_idx - 1)
        sort_last_as_pivot(array, left_idx + 1, end_idx)
    else:
        sort_last_as_pivot(array, left_idx + 1, end_idx)
        sort_last_as_pivot(array, start_idx, left_idx - 1)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    # print(quickSort([-2, 3, 2, 4, - 1, 1, 0, -1, 9, -10]))
    print(quickSort([-1, 8, 5, 2, 9, 5, 6, 3]))

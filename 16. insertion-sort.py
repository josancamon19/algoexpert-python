# def insertionSort(array):
#     for i in range(0, len(array) - 1):
#         this_idx = i
#         next_idx = i + 1
#
#         while this_idx >= 0 and array[next_idx] < array[this_idx]:  # is next less than this
#             array[this_idx], array[next_idx] = array[next_idx], array[this_idx]
#             next_idx -= 1
#             this_idx -= 1
#     return array

def insertionSort(array):
    for i in range(0, len(array) - 1):
        while i >= 0 and array[i + 1] < array[i]:  # is next less than this
            array[i], array[i + 1] = array[i + 1], array[i]
            i -= 1
    return array


if __name__ == '__main__':
    print(insertionSort([3, 2, 1, 0]))

def mergeSort(array):
    for i, item in enumerate(array):
        array[i] = [item]

    print(array)


def divide_array(array):
    pass


def sort_pair_arrays(array1, array2):
    if array1 is None or len(array1) == 0:
        return array2
    if array2 is None or len(array2) == 0:
        return array1

    new_array = []
    first_idx, second_idx = 0, 0
    while first_idx < len(array1) or second_idx < len(array2):

        if first_idx >= len(array1):
            new_array += array2[second_idx:]
            break

        if second_idx >= len(array2):
            new_array += array1[first_idx:]
            break

        first = array1[first_idx]
        second = array2[second_idx]

        if first <= second:
            new_array.append(first)
            first_idx += 1
        elif second < first:
            new_array.append(second)
            second_idx += 1

    return new_array


if __name__ == '__main__':
    print(mergeSort([8, 2, 5, 9, 5, 6, 3]))
    # print(sort_pair_arrays([1], [2]))

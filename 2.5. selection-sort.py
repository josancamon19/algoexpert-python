def get_min(array):
    # print('Array to get min:', array)
    min_element = None
    for idx, value in enumerate(array):
        if min_element is None or value < min_element[1]:
            min_element = idx, value

    # print('Getting min element', min_element)
    return min_element[0]


def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        min_idx = get_min(array[i:]) + i
        # print(array[i], array[min_idx], array)
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


if __name__ == '__main__':
    print(selectionSort([3, 2, 1, 0]))

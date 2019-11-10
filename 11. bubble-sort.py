def bubbleSort(array):
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    print(bubbleSort([4, 3, 2, 1]))
    # print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))

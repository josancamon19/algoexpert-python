def binarySearch(array, target):
    # Write your code here.
    first = 0
    last = len(array) - 1
    while True:

        mid_idx = (last + first) // 2
        mid_element = array[mid_idx]

        if mid_element == target:
            return mid_idx
        elif first == last or first > last:
            return -1
        elif mid_element > target:
            last = mid_idx
        else:  # mid_element < target
            first = mid_idx + 1


if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binarySearch(a, 5))

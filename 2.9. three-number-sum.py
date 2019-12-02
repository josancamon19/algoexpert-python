def threeNumberSum(array, targetSum):
    array.sort()  # nlogn
    results = []
    for current in range(len(array)):
        left = current + 1
        right = len(array) - 1
        while left < right:
            result = array[current] + array[left] + array[right]
            if result == targetSum:
                results.append([array[current], array[left], array[right]])
                left += 1
                right -= 1
            elif result < targetSum:
                left += 1
            else:
                right -= 1
    return results


if __name__ == '__main__':
    print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
    print(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33))
    print(threeNumberSum([1], 10))
    print(threeNumberSum([1, 2, 3, 7, 0], 10))

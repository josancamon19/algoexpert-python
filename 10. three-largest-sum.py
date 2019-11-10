# def findThreeLargestNumbers(array):
#     # Write your code here.
#     return sorted(array)[-3:]  # sorted -> O(logn)
#
# find_three_largest = lambda array: sorted(array)[-3:]


# def findThreeLargestNumbers(array):
#     # Write your code here.
#     result = array[:3]
#     for n in array[3:]:
#         min_result = min(result)
#         if n > min_result:
#             result[result.index(min_result)] = n
#
#     return sorted(result)


# This solution works for n largest len of result
def findThreeLargestNumbers(array):
    # Write your code here.
    result = [None for _ in range(3)]
    for number in array:
        for i in range(len(result)):
            idx = len(result) - 1 - i
            print(number, result)
            if result[idx] is None:
                result[idx] = number
                break
            elif result[idx] < number:
                this = result[idx]
                if idx > 0:
                    # TODO here go idx --- 0 and swapping nodes throwing 0
                    result[idx - 1] = result[idx]
                result[idx] = number
                break

    return result


if __name__ == '__main__':
    print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
    # print(findThreeLargestNumbers([1, 2, 3, 4]))

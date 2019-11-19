# def smallestDifference(arrayOne, arrayTwo):  # O(n2)
#     # Write your code here.
#     smallest = [float('inf'), float('-inf')]
#     for one in arrayOne:
#         for two in arrayTwo:
#             if abs(smallest[0] - smallest[1]) > abs(one - two):
#                 smallest = [one, two]
#     return smallest

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    smallest = [float('inf'), float('-inf')]
    first_idx = 0
    second_idx = 0
    while True:
        first = arrayOne[first_idx]
        second = arrayTwo[second_idx]
        expected = abs(first - second)

        if abs(smallest[0] - smallest[1]) > expected:
            smallest = [first, second]

        if first == second:
            break
        elif first < second:
            if first_idx + 1 < len(arrayOne):
                first_idx += 1
            else:
                break
        else:  # first > second
            if second_idx + 1 < len(arrayTwo):
                second_idx += 1
            else:
                break

    return smallest


if __name__ == '__main__':
    smallestDifference([1, 2, 3, 4], [3, 2, 1])

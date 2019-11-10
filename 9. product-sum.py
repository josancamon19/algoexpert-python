def productSum(array):
    # Write your code here.
    return product_sum_with_depth(array)


def product_sum_with_depth(array, depth=1):
    to_add = 0
    for item in array:
        if type(item) is list:
            to_add += (depth + 1) * product_sum_with_depth(item, depth + 1)
        else:
            to_add += item
    return to_add


if __name__ == '__main__':
    print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
    # print(productSum([6, [-13, 8], 4]))

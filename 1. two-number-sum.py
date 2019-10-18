def two_number_sum(array, target_sum):
    for n in array:
        residual = target_sum - n
        if residual in array and residual != n:
            return sorted([residual, n])
    return []


if __name__ == '__main__':
    print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))

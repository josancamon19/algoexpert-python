from copy import copy


def getPermutations(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return [array]
    permutations = []
    for i, item in enumerate(array):
        array[0], array[i] = array[i], array[0]
        permutations.append(copy(array))


    return permutations


if __name__ == '__main__':
    print(len(getPermutations([1, 2, 3, 4])))


def getPermutations(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return [array]
    permutations = []

    for i in range(len(array)):
        array.insert(0, array.pop(i))
        for perm in getPermutations(array[1:]):
            perm.insert(0, array[0])
            permutations.append(perm)

    return permutations


if __name__ == '__main__':
    print(getPermutations([1, 2, 3, 4]))

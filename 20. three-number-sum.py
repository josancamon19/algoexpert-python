from collections import Counter


def threeNumberSum(array, targetSum):
    items = dict(Counter(array))
    for item1, counter1 in items.items():
        if counter1 > 0:
            for item2, counter2 in items.items():
                item3_expected = targetSum - item1 - item2
                if (item1 == item2 or item1 == item3_expected or item2 == item3_expected) and counter2 < 2:
                    continue
                if item3_expected in items:
                    print(item1, item2, item3_expected)


if __name__ == '__main__':
    threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)

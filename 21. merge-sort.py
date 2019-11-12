def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array
    mid_idx = len(array) // 2
    left = array[:mid_idx]
    right = array[mid_idx:]
    l = mergeSort(left)
    r = mergeSort(right)
    # print(l, r)
    print(merge_sorting(l, r))


def merge_sorting(left, right):
    if left is None and right is None:
        return []
    elif left is None:
        return right
    elif right is None:
        return left
    else:
        left_idx = 0
        right_idx = 0
        sorted_list = []
        while left_idx < len(left) or right_idx < len(right):
            if left_idx >= len(left):
                sorted_list += right[right_idx:]
                break
            elif right_idx >= len(right):
                sorted_list += left[left_idx:]
                break
            else:
                if left[left_idx] < right[right_idx]:
                    sorted_list.append(left[left_idx])
                    left_idx += 1
                else:
                    sorted_list.append(right[right_idx])
                    right_idx += 1

        return sorted_list


if __name__ == '__main__':
    print(mergeSort([8, 5, 2, 9, 5, 6, 3]))
    # print(merge_sorting([1], [2]))

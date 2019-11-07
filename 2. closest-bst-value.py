def compare(node_value, target):
    if node_value > target:
        return -1
    elif node_value < target:
        return 1
    else:
        return 0


def find_closest_value_in_bst(tree, target):
    node = tree.root

    while node:
        comparision = compare(node.value, target)
        if comparision == -1:
            if node.left:
                node = node.left
            else:
                return node.value
        elif comparision == 1:
            if node.right:
                node = node.right
            else:
                return node.value

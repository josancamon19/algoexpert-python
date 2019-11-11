def findClosestValueInBst(tree, target):
    closest_value = float('inf')
    node = tree
    while node:
        if abs(target - closest_value) > abs(target - node.value):
            closest_value = node.value

        if node.value > target:
            if node.left is None:
                return closest_value
            node = node.left

        elif node.value < target:
            if node.right is None:
                return closest_value
            node = node.right

        else:
            return node.value

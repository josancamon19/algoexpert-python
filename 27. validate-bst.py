def validateBst(node, less_than=float('inf'), greater_than=float('-inf')):
    if node is None:
        return True
    if greater_than <= node.value < less_than:
        left_validation = validateBst(node.left, node.value, greater_than)
        right_validation = validateBst(node.right, less_than, node.value)
        return left_validation and right_validation
    return False

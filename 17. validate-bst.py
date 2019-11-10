# def compare(node_value, target):
#     if node_value > target:
#         return -1
#     elif node_value < target:
#         return 1
#     else:
#         return 0
#
#
# def validateBst(node):
#     # Write your code here.
#     if (node.left is None or node.value > node.left.value) and (node.right is None or node.value <= node.right.value):
#         return validateBst()
# def findClosestValueInBst(tree, target):
#     # Write your code here.
#     parent_node = None
#     node = tree
#     while node:
#         if node.value > target:
#             if node.left:
#                 node = node.left
#             else:
#                 node = node.right
#         elif node.value < target:
#             if node.right:
#                 node = node.right
#             else:
#                 return node.value

def compare(node_value, target):
    if node_value > target:
        return -1
    elif node_value < target:
        return 1
    else:
        return 0


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def traverse(self, node):
        visit_order = list()
        if node:
            visit_order.append(node.value)
            visit_order += self.traverse(node.left)
            visit_order += self.traverse(node.right)
        return visit_order

    def insert(self, value):

        new_node = BST(value)
        node = BST(self.value)
        while True:
            comparision = compare(node.value, value)
            if comparision == -1:
                if self.left:
                    node = self.left
                else:
                    self.left = new_node
                    break
            elif comparision == 1:
                if self.right:
                    node = self.right
                else:
                    self.right = new_node
                    break
            else:
                self.value = value
                break

        return self

    def contains(self, value):
        node = BST(self.value)
        while True:
            comparision = compare(node.value, value)
            if comparision == -1:
                if self.left:
                    node = self.left
                else:
                    break
            elif comparision == 1:
                if self.right:
                    node = self.right
                else:
                    break
            else:
                return node

        return None

    def remove(self, value):
        node = BST(self.value)
        while True:
            comparision = compare(node.value, value)
            if comparision == -1:
                if self.left:
                    node = self.left
                else:
                    print('Value not found')
                    break
            elif comparision == 1:
                if self.right:
                    node = self.right
                else:
                    print('Value not found')
                    break
            else:
                if node.left:
                    new_node = max(self.traverse(node.left))
                    pass
                elif node.right:
                    new_node = min(self.traverse(node.right))
                    # swap nodes
                else:
                    del node
                    break

        return self


if __name__ == '__main__':
    pass
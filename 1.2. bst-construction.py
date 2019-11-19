def traverse_list(node):
    visit_order = list()
    if node:
        visit_order.append(node.value)
        visit_order += traverse_list(node.left)
        visit_order += traverse_list(node.right)
    return visit_order


def traverse(node):
    visit_order = list()
    if node:
        visit_order.append(node)
        visit_order += traverse(node.left)
        visit_order += traverse(node.right)
    return visit_order


def get_min_node_value(node):
    while node.left:
        node = node.left
    return node.value


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def compare(self, target):
        if self.value > target:
            return -1
        elif self.value < target:
            return 1
        else:
            return 0

    def insert(self, value):

        node = self
        while True:
            comparision = node.compare(value)
            if comparision == -1:
                if node.left:
                    node = node.left
                else:
                    node.left = BST(value)
                    break
            else:  # comparision == 1 or equals
                if node.right:
                    node = node.right
                else:
                    node.right = BST(value)
                    break

        return self

    def contains(self, value):
        node = self
        while node:
            comparision = node.compare(value)
            if comparision == -1:
                node = node.left
            elif comparision == 1:
                node = node.right
            else:
                return True

        return False

    def remove(self, value, parent_node=None):
        node = self
        while True:
            comparision = node.compare(value)
            if comparision == -1:
                if node.left:
                    parent_node = node
                    node = node.left
                else:
                    print('Value not found')
                    break
            elif comparision == 1:
                if node.right:
                    parent_node = node
                    node = node.right
                else:
                    print('Value not found')
                    break
            else:
                if node.left and node.right:  # node with left and child
                    node.value = get_min_node_value(node.right)
                    node.right.remove(node.value, node)
                elif parent_node is None:  # parent node
                    if node.left:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:  # parent node with no children
                        node.value = None

                elif parent_node.left == node:  # found in the left node with right None
                    parent_node.left = node.left if node.left else node.right
                elif parent_node.right == node:  # found in the right node with left None
                    parent_node.right = node.left if node.left else node.right
                break

        return self


if __name__ == '__main__':
    # tree = BST(10)
    # tree.insert(5)
    # tree.insert(8)
    # tree.insert(3)
    # tree.insert(4)
    # tree.insert(1)
    # tree.insert(2)
    # tree.insert(0)
    # print(traverse_list(tree))
    #
    # tree.remove(5)
    # print(traverse_list(tree))
    test = BST(10).insert(5).insert(7).insert(2).remove(10)
    print(traverse_list(test))

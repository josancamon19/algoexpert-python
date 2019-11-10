class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(-1)
            array.append(node.name)
            for child in node.children:
                queue.insert(0, child)

        return array


if __name__ == '__main__':
    test1 = Node('A').addChild('B').addChild('C').addChild('D')
    test1.children[0].addChild('E').addChild('F')
    test1.children[2].addChild('G').addChild('H')
    test1.children[0].children[1].addChild('I').addChild('J')
    test1.children[2].children[0].addChild('K')

    print(test1.breadthFirstSearch([]))

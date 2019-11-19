class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def __repr__(self):
        return str(self.name)

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for n in self.children:
            n.depthFirstSearch(array)
        return array


if __name__ == '__main__':
    root = Node('A')

    root.addChild('B')
    root.addChild('C')
    root.addChild('D')

    # append to B node E and F
    root.children[0].addChild('E')
    root.children[0].addChild('F')

    # append to D node G and H
    root.children[2].addChild('G')
    root.children[2].addChild('H')

    # append to F node I and J
    root.children[0].children[1].addChild('I')
    root.children[0].children[1].addChild('J')

    # append K to G node
    root.children[2].children[0].addChild('K')

    print(root.depthFirstSearch([]))

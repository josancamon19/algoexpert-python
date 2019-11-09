# Feel free to add new properties and methods to the class.
# noinspection PyPep8Naming
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)

    def get_prev_value(self):
        if self.prev is None:
            return 'None'
        return str(self.prev.value)

    def get_next_value(self):
        if self.next is None:
            return 'None'
        return str(self.next.value)

    def __str__(self):
        return 'Node(prev:' + self.get_prev_value() + ', this:' + str(
            self.value) + ', next:' + self.get_next_value() + ')'

    def __eq__(self, other):
        if other:
            return self.value == other.value
        return self is None


# noinspection PyPep8Naming
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.

        if self.tail is None:
            self.setHead(node)
            return

        self.insertAfter(self.tail, node)

    def append(self, node):
        if self.head is None:
            self.setHead(node)
            return

        current = self.head
        while current.next is not None:
            current = current.next

        node.prev = current
        current.next = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return
        current = self.head
        index = 1
        while current and position != index:
            index += 1
            current = current.next

        if current is None:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(current, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        current = self.head
        while current:
            nxt = current.next
            if current.value == value:
                self.remove(current)

            current = nxt

    def remove(self, node):
        # Write your code here.

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev

        self.removeNode(node)

    def removeNode(self, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

        del node

    def containsNodeWithValue(self, value):
        # Write your code here.

        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __repr__(self):

        if self.head is None:
            return '---<Empty>---'

        statement = ''
        current = self.head
        while current:
            statement += str(current)
            current = current.next
            if current:
                statement += ' ---> '

        return statement + ''

# Initial Wrong solution
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def setHead(self, node):
#         # Write your code here.
#
#         if self.head is not None:
#             self.head.prev = node
#
#         node.next = self.head
#         self.head = node
#
#     def setTail(self, node):
#         # Write your code here.
#
#         if self.head is None:
#             self.head = node
#
#         if self.tail is not None:
#             self.tail.next = node
#
#         node.prev = self.tail
#         self.tail = node
#         return self.head
#
#     def append(self, node):
#         if self.head is None:
#             self.setHead(node)
#             return
#
#         current = self.head
#         while current.next is not None:
#             current = current.next
#
#         node.prev = current
#         current.next = node
#
#     def insertBefore(self, node, nodeToInsert):
#         # Write your code here.
#         if node == self.head:
#             self.setHead(nodeToInsert)
#             return
#
#         current = self.head
#         while current.next:
#             if current.next == node:  # TODO check if use .value or not
#                 nodeToInsert.prev = current
#                 nodeToInsert.next = current.next
#
#                 current.next.prev = nodeToInsert
#                 current.next = nodeToInsert
#                 break
#             current = current.next
#
#     def insertAfter(self, node, nodeToInsert):
#         # Write your code here.
#         current = self.head
#         while current.next:
#             if current.next == node:  # TODO check if use .value or not
#                 nodeToInsert.prev = current.next
#                 nodeToInsert.next = current.next.next
#
#                 if current.next.next:
#                     current.next.next.prev = nodeToInsert
#                 current.next.next = nodeToInsert
#                 break
#             current = current.next
#
#     def insertAtPosition(self, position, nodeToInsert):
#         # Write your code here.
#         if position == 1:
#             self.setHead(nodeToInsert)
#             return
#         current = self.head
#         index = 1
#         while current:
#             if position == index + 1:
#                 nodeToInsert.prev = current
#                 nodeToInsert.next = current.next
#                 if current.next:
#                     current.next.prev = nodeToInsert
#                 current.next = nodeToInsert
#                 break
#             index += 1
#             current = current.next
#
#     def removeNodesWithValue(self, value):
#         # Write your code here.
#         current = self.head
#         while current:
#             if current.value == value:
#                 if current.prev:
#                     current.prev.next = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#
#             current = current.next
#
#     def remove(self, node):
#         # Write your code here.
#         current = self.head
#         while current:
#             if current == node:
#                 if current.prev:
#                     current.prev.next = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#                 break
#
#             current = current.next
#
#     def containsNodeWithValue(self, value):
#         # Write your code here.
#         if self.head is None:
#             return False
#
#         current = self.head
#         while current:
#             if current.value == value:
#                 return True
#             current = current.next
#         return False
#
#     def __repr__(self):
#         if self.head is None:
#             return '---<Empty>---'
#
#         statement = ''
#         current = self.head
#         while current:
#             statement += str(current)
#             current = current.next
#             if current:
#                 statement += ' ---> '
#
#         return statement + ''
#
#
# if __name__ == '__main__':
#     doubly = DoublyLinkedList()
#
#     doubly.append(Node(1))
#     doubly.append(Node(2))
#     doubly.append(Node(4))
#     # print(doubly)
#
#     doubly.insertBefore(Node(4), Node(3))
#     # print(doubly)
#
#     doubly.insertAfter(Node(4), Node(5))
#     # print(doubly)
#
#     doubly.remove(Node(3))
#     # print(doubly)
#
#     doubly.append(Node(2))
#     doubly.append(Node(2))
#     # print(doubly)
#
#     doubly.removeNodesWithValue(2)
#     print(doubly)
#
#     doubly.insertAtPosition(2, Node(2))
#     print(doubly)
#
#     doubly.insertAtPosition(3, Node(3))
#     print(doubly)
#
#     doubly.insertAtPosition(6, Node(6))
#     print(doubly)
#
#     doubly.insertAtPosition(2, Node(1.5))
#     print(doubly)

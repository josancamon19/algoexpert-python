def reverseLinkedList(head):
    # Write your code here.
    previous = None
    current = head
    while current:
        nxt = current.next
        current.next = previous
        previous = current
        if nxt is None:
            break
        current = nxt
    return current

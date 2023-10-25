def sortedInsert(head, x):
    h = head
    node = Node(x)
    if not head:
        return node
    elif head.data >= x:
        node.next = head
        node.next.prev=node
        return node
    curr = head
    while curr.next and curr.next.data<x:
        curr=curr.next
    node.next=curr.next
    if curr.next:
        node.next.prev=node
    curr.next=node
    node.prev=curr

    return head

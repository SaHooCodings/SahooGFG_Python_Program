def insertInMid(head,new_node):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    new_node.next = slow.next
    slow.next = new_node

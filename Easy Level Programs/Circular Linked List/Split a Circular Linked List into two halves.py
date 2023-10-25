'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList(self, head, head1, head2):
        if head == None: 
            return
        fast = head 
        slow = head 
        while fast.next != head and fast.next.next != head:
            fast = fast.next.next
            slow = slow.next
        if fast.next.next == head:
            fast = fast.next

        head1 = head 
        head2 = slow.next

        fast.next = slow.next 
        slow.next = head
        return head1,head2

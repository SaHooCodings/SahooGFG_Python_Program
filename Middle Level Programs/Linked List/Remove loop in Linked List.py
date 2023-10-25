class Solution:
    def removeLoop(self, head):
        fast = head.next
        slow = head
        
        while fast!=slow:
            if fast is None or fast.next is None:
                return
            
            fast = fast.next.next
            slow = slow.next
        
        size = 1
        fast = fast.next
        while fast!=slow:
            fast = fast.next
            size+=1
        slow=head
        fast=head
        for _ in range(size-1):
            fast=fast.next
        while fast.next != slow:
            fast=fast.next
            slow=slow.next
        fast.next=None

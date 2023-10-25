class Solution:    
    def reverse(self,head):
    # this function reverses the linked list
        prev = None
        current = head
        next = head.next
        
        while current is not None:
            next = current.next       # storing next node
            current.next = prev       # linking current node to previous
            prev = current            # updating prev
            current = next            # updating current
        
        return prev
    
    def addOne(self,head):
        head = self.reverse(head)          
        
        current = head
        carry = 1
        
        while(carry):
            current.data += 1   
            
            if current.data < 10:
                return self.reverse(head)
            else:
                current.data = 0
            
            if current.next is None:
                break
            else:
                current = current.next
        current.next = Node(1)     
        return self.reverse(head)

class Solution:
    def reverseDLL(self, head): 
        # Initialize temporary variables
        temp = None
        current = head 
    
        # Reverse the doubly linked list
        while current is not None: 
            # Swap previous and next pointers of the current node
            temp = current.prev  
            current.prev = current.next
            current.next = temp 
            current = current.prev 
    
        # Update the head if necessary
        if temp is not None: 
            head = temp.prev
        return head

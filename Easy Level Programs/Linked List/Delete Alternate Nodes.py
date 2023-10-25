class Solution: 
    
    # Function to delete alternate nodes
    def deleteAlt(self, head):
        
        # Loop through the linked list
        while head is not None:
            # Check if there is a next node
            if head.next is not None:
                # Remove the next node by skipping it
                head.next = head.next.next
            
            # Move to the next node
            head = head.next

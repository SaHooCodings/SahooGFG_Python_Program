class Solution:

    def insertAtBegining(self,head,x):
        
        temp = Node(x)
        if head is None:
            return temp
            
        temp.next = head
        
        return temp
    
    def insertAtEnd(self,head,x):
        temp = Node(x)
        if head is None:
            return temp
            
        ptr = head
        while ptr.next:
            ptr=ptr.next;
            
        ptr.next = temp;
        
        return head

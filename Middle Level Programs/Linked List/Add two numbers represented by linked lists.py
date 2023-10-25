''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to reverse the linked list.
    def reverse(self, head):
        prev = None
        current = head
        next = None
        
        while current is not None:
            next = current.next      
            current.next = prev   
            prev = current       
            current = next    
        
        return prev
    def addTwoLists(self, first, second):
        
        first = self.reverse(first)  
        second = self.reverse(second)  
        
        sumList = None
        carry = 0
        
        while first is not None or second is not None or carry>0:
            newVal = carry
            
            if first is not None:
                newVal += first.data
            if second is not None:
                newVal += second.data

            carry = newVal//10
            newVal = newVal%10       
            newNode = Node(newVal)
            newNode.next = sumList
            sumList = newNode
            if first:
                first = first.next    
            if second:
                second= second.next
        
        return sumList

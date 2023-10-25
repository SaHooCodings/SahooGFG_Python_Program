class Solution:
    def getSize(self, head):
        count = 0
        curr_node = head
        while curr_node:
            count +=1
            curr_node = curr_node.next
        return count
    def splitList(self, source): 
        if source == None or source.next == None:
            frontRef = source
            backRef = None
        else:
            size = self.getSize(source)
            length = (size+1)//2
    
            frontRef = source
            while length>1:
                length-=1
                frontRef = frontRef.next
    
            backRef = frontRef.next
            frontRef.next = None
        return [source,backRef]
    def mergeList(self, head_a,head_b):
        result = LinkedList()
        if head_a == None:
            return head_b
        if head_b == None:
            return head_a
        if head_a.data <= head_b.data:
            result.head = head_a
            result.head.next = self.mergeList(head_a.next,head_b)
        else:
            result.head = head_b
            result.head.next = self.mergeList(head_a, head_b.next)
        
        return result.head
    def mergeSort(self, head):
       
        a = LinkedList()
        b = LinkedList()
    
        if head == None or head.next == None:
            return head
        node_list = self.splitList(head) 
        a.head = node_list[0] 
        b.head = node_list[1] 
        a.head = self.mergeSort(a.head) 
        b.head = self.mergeSort(b.head)
        return self.mergeList(a.head,b.head)

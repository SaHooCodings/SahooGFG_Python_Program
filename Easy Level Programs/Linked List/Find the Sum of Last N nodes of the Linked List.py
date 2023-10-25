def sumOfLastN_Nodes(head,n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    # Traverse n nodes from the beginning
    while n :
        if n and curr_node == None:
            return 0
        curr_node = curr_node.next
        n-=1

    # Traverse till the end of the list
    while curr_node :
        curr_node = curr_node.next
        nth_node = nth_node.next
        
    sm=0
    
    # Calculate the sum of data of the last n nodes
    while nth_node:
        sm+=nth_node.data
        nth_node=nth_node.next

    # Return the sum
    return sm

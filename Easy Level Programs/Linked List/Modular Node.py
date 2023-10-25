def modularNode(head, k): 
      
    # Corner cases 
    if (k <= 0 or head == None): 
        return None
  
    # Traverse the given list 
    i = 1
    modularNode = None
    temp = head 
    while (temp != None): 
        if (i % k == 0): 
            modularNode = temp 
  
        i = i + 1
        temp = temp.next
    if i<k:
        return -1
    return modularNode.data

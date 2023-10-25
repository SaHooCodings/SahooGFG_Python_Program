def isCircular(head):
    
    temp = head.next;
    while(temp!=None and temp!=head):
        temp=temp.next;
    return temp==head

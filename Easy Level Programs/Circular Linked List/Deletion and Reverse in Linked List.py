def deleteNode(head, key):
    #your code goes here
    temp=head
    while temp:
        if temp.next.data==key:
            temp.next=temp.next.next
            break
        temp=temp.next
    return head
def reverse(head):
    if head:
        t11=head
        while t11.next!=head:
            t11=t11.next
        t1=t11
        temp=head
        
        while temp.next!=head:
            t2=temp
            temp=temp.next
            t2.next=t1
            t1=t2
        temp.next=t1
        temp1=head
        while temp1.next!=head:
            t=temp1.data
            temp1.data=temp1.next.data
            temp1.next.data=t
            temp1=temp1.next

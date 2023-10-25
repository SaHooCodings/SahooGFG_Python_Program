def getNth(head, k):
    cur = head
    cnt = 1
    while(cur is not None):
        if(cnt==k):
            return cur.data
        cnt+=1
        cur=cur.next

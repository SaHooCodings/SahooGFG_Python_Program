class Solution:
    def rotate(self, head, k):
        if k == 0:
            return head
        
        walk = head
        prev = None
        for _ in range(k):
            prev = walk
            walk = walk.next
            if walk is None:
                return head
        newHead = walk
        prev.next = None
        while walk.next is not None:
            walk = walk.next
        walk.next = head
        return newHead

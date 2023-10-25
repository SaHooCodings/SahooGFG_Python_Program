class Solution:
    def getCount(self, head_node):
        curr_node=head_node
        count=0
        while curr_node:
            count+=1
            curr_node=curr_node.next
        return count

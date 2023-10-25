class Solution:
    def display(self,node):
        while node:
            print(node.data, end=" ")
            node = node.next

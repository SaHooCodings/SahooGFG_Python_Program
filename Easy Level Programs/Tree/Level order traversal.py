"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""

class Solution:
    def levelOrder(self,root):
        
        res = []
        if root is None:
            return res
        que = []
        que.append(root)
        
        while 1:
            n = len(que)
            if n==0:
                break
            while(n>0):
                node = que.pop(0)
                res.append (node.data)
                if node.left != None:
                    que.append(node.left)
                if node.right != None:
                    que.append(node.right)
                n-=1
        return res

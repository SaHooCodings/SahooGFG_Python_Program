class Solution:
    def inorderUtil (self,root, res):
        if root is None:
            return
        self.inorderUtil(root.left, res) 
        res.append (root.data)
        self.inorderUtil(root.right, res)
    def InOrder(self,root):
        res = []
        self.inorderUtil (root, res)
        #returning the list.
        return res

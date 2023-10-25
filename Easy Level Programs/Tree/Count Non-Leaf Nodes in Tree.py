class Solution:
    
    #Function to count the number of non-leaf nodes in a binary tree.
    def countNonLeafNodes(self, root):
        
        #If root is None, return 0
        if(root is None):
            return 0
        
        #If root has no left or right child, return 0
        if(root.left is None and root.right is None):
            return 0
        
        #Recursively count non-leaf nodes in the left and right subtrees
        return 1 + self.countNonLeafNodes(root.left) + self.countNonLeafNodes(root.right)

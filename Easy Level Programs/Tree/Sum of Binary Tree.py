def sumBT(root):
    # Check if the root is None, return 0 if so
    if(root==None):
        return 0
    
    # Recursively calculate the sum of the left subtree, right subtree, and the current node
    return (root.data+sumBT(root.left)+sumBT(root.right))  

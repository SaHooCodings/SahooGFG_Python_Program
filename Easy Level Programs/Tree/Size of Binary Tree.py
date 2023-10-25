def getSize(node):
    # Base condition: If node is None, return size as 0
    if (node is None):
        return (0)
    else:
        # Recursively calculate and return the size of the tree
        return (getSize(node.left)+ 1 +getSize(node.right))

def minValue(root):
    
    #base case
    if root is None:
        return -1
    temp=root
    while(temp.left is not None):
        temp=temp.left
    return temp.data

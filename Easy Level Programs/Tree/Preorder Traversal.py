def preorderUtil(root, res):
    if root is None: 
        return
    res.append (root.data)
    preorderUtil(root.left, res)
    preorderUtil(root.right, res)
def preorder (root):
    res = []
    preorderUtil (root, res)
    #returning the list.
    return res

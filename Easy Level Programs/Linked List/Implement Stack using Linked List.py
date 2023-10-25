class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def push(self, data):
        
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        return
    def pop(self):
        if (self.isEmpty()):
            return -1
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return -1
        return self.root.data

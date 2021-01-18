class Node:
    def __init__(self, val):
        self.childleft = None
        self.childright = None
        self.nodedata = val


root = Node(1)
root.childleft = Node(3)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)



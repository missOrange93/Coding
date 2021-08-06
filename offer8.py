class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i
i.parent = e
h.parent = e
f.parent = c
g.parent = c
d.parent = b
e.parent = b
b.parent = a
c.parent = a

def inOrderTraverse(node):
    if not node:
        return None
    inOrderTraverse(node.left)
    nodes.append(node)
    inOrderTraverse(node.right)

def FindNext(node):
    global nodes
    nodes = []
    root = node
    while root.parent:
        root = root.parent
    inOrderTraverse(root)
    for i in range(0,len(nodes)):
        if nodes[i] == node:
            return nodes[i+1].val

print(FindNext(i))
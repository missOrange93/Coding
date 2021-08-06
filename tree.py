#二叉查找树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

def preOrderTraverse(node):
    if not node:
        return None
    print(node.val)
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)

def inOrderTraverse(node):
    if not node:
        return None
    inOrderTraverse(node.left)
    print(node.eval)
    inOrderTraverse(node.right)

def postOrderTraverse(node):
    if not node:
        return None
    postOrderTraverse(node.left)
    postOrderTraverse(node.right)
    print(node.eval)

def layerTraverse(node):
    if not node:
        return None
    queue = []
    queue.append(node)
    while len(queue) > 0:
        tmp = queue.pop(0)
        print(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.right)


def insert(root,val):
    if not root:
        root = TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left,val)
        elif val > root.vol:
            root.right = insert(root.right,val)
    return root

def query(root,val):
    if not root:
        return False
    elif root.val == val:
        return True
    elif val < root.val:
        return query (root.left,val)
    elif val > root.val:
        return query(root.right,val)

def findMin(root):
    if not root:
		return None
    elif root.left:
		return findMin(root.left)
    else:
		return root

def findMax(root):
	if not root:
		return None
	elif root.right:
		return findMax(root.right)
	else:
		return root

def delNode(root,val):
    if not root:
        return None
    elif val < root.val:
        root.left = delNode(root.left,val)
    elif val > root.val:
        root.right = delNode(root.right,val)
    else:
        if (root.left == None) and (root.right ==None):
            root = None
        elif root.left and root.right:
            temp = findMin(root.right)
            root.val = temp.val
            root.right = delNode(root.right, temp.val)
        elif root.left == None:
            root.val = root.right.val
            root.left = root.right.left
            root.right = root.right.right
        elif root.right == None:
            root.val = root.left.val
            root.left = root.left.left
            root.right = root.left.right
    return root    #返回需要删除的节点位置上目前的节点

#平衡二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.bf = 0
        self.left = None
        self.right = None


def LL(a,b):
    a.left = b.right  # 将b的右子树接到a的左子结点上
    b.right = a  #将a树接到b的右子结点上
    a.bf = b.bf =0
    return b

def RR(a,b):
    a.right = b.left
    b.left = a
    a.bf =b.bf =0
    return b

def LR(a,b):
    c = b.right
    a.left, b.right = c.right, c.left
    c.left, c.right = b,a
    if c.bf == 0: #c本身就是插入点
        a.bf = b.bf = 0
    elif c.bf ==1: #插在c的左子树
        a.bf = -1
        b.bf = 0
    else:           #插在c的右子树
        a.bf = 0
        b.bf = 1
    c.bf = 0
    return c


def RL(a, b):
    c = b.left
    a.right, b.left = c.left, c.right
    c.left, c.right = a, b
    if c.bf == 0:
        a.bf = b.bf = 0
    elif c.bf == 1:
        a.bf = 0
        b.bf = -1
    else:
        a.bf = 1
        b.bf = 0
    c.bf = 0
    return c


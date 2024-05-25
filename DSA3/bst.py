class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insert(root,value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root


root = None

# val = [5,7,4,3,2,8,1]
# for vl in val:
root= insert(root,5)
root= insert(root,7)
root= insert(root,4)
root= insert(root,3)
root= insert(root,8)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end='')
        inorder(node.right)
def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value,end='')
def search(root,target):
    if not root or root.value == target:
        return root
    if target<root.value:
        return search(root.left,target)
    return search(root.right, target)

res = search(root,10)
if res:
    print(True)
else:
    print(False)

def min(node):
    current = node
    while current.left:
        current = current.left
    return
def delt(root,target):
    if root is None:
        return root
    if target<root.value:
        root.left = delt(root.left,target)
    elif target>root.value:
         root.right = delt(root.right,target)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        root.value = min(root.right).value
        root.right = delt(root.right,root.value)
    return root

# delt(root,3)
print(inorder(root))
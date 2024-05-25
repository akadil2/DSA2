class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def height(node):
    if not node:
        return 0
    else:
        right_h = height(node.right)
        left_h = height(node.left)
        return max(right_h,left_h)+1

print(height(root))

def preorder(node):
    if node:
        print(node.value, end='')
        preorder(node.left)
        preorder(node.right)
preorder(root)

def search(root,target):
    if not root or root.value == target:
        return root
    
    left_result=search(root.left,target)
    if left_result:
        return left_result
    return search(root.right, target)

res = search(root,7)
if res:
    print('found')
else:
    print('not found')
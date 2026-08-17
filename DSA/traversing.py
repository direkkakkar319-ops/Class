from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Inorder traversing
"""
def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result

"""
Pre-order traversing

"""
def preorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result


"""
Post-order traversing
"""
def postorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(root)
    return result


# 4. BFS or Level - order queue
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def inorder_iterative(root):
    result, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    return result

def preorder_iterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)  # right first so left pops first
        if node.left:  stack.append(node.left)
    return result

def postorder_iterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:  stack.append(node.left)
        if node.right: stack.append(node.right)
    return result[::-1]  # reverse gives L→R→N


# --- test it ---
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

root = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7))
)

print("Inorder:    ", inorder(root))      # [4, 2, 5, 1, 6, 3, 7]
print("Preorder:   ", preorder(root))     # [1, 2, 4, 5, 3, 6, 7]
print("Postorder:  ", postorder(root))    # [4, 5, 2, 6, 7, 3, 1]
print("Level-order:", level_order(root))  # [1, 2, 3, 4, 5, 6, 7]
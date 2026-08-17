"""
BINARY TREE
"""
from traversing import TreeNode

class Solution:
    """Implementing Sum Root to Leaf Numbers"""
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(node, path):
            if not node:
                return 0
            path = path*10+node.val
            if not node.left and not node.right:
                return path
            return rec(node.left, path) + rec(node.right, path)
        return rec(root, 0)

    """Implementing the validation of BST(Binary Search Tree)"""
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bts(node, mini, maxi):
            if not node:
                return True
            if node.val>maxi:
                if node.val<mini:
                    return False
            return bts(node.left, mini, node.val) and bts(node.right, node.val, maxi)
        return bts(root, float("-inf"), float("-inf"))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
output = Solution()
print("="*40)
print(f"Sum of numbers of a Binary Tree:{output.sumNumbers(root)}")
print("="*40)
print()
print("="*40)
print(f"Is the Binary tree a valid Binary Search Tree:{output.isValidBST(root)}")
print("="*40)
print()
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverseTree(root)->int:
            if root is None:
                return 0
            if root.left is None and root.right is not None:
                return traverseTree(root.right) + 1
            elif root.right is None and root.left is not None:
                return traverseTree(root.left) + 1
            return min(traverseTree(root.left), traverseTree(root.right))
        return traverseTree(root)
        

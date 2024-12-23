# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverseTree(root, depth: int) -> int:
            if root is None:
                return depth
            return max(traverseTree(root.left, depth+1), traverseTree(root.right, depth+1))
        return traverseTree(root, 0)
        

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(root, sumPath):
            if root is None:
                return False
            sumPath += root.val
            # if there is a leaf check if is the target
            if root.left is None and root.right is None:
                return sumPath == targetSum
            return traverse(root.left, sumPath) or traverse(root.right, sumPath)
        return traverse(root, 0)

        

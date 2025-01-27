# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverseTree(root: Optional[TreeNode]):
            if not root:
                return None
            if root.val == val:
                return root
            left = traverseTree(root.left)
            if left is not None:
                return left
            right = traverseTree(root.right)
            if right is not None:
                return right
            return None
        return traverseTree(root)


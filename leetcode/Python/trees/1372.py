# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def traverse(root, isLeft:int, current:int):
            if root is None:
                return
            self.max_length = max(self.max_length, current)
            if isLeft == 1:
                traverse(root.right, 0,current+1)
                traverse(root.left, 1, 1)
            else:
                traverse(root.left, 1, current+1)
                traverse(root.right,0,1)
        traverse(root,1,0)
        traverse(root,0,0)
        return self.max_length
        

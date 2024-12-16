# Definition for a binary tree node.
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Values = {}

        def traverse(root, depth: int):
            if root is None:
                return
            if depth in Values:
                Values[depth].append(root.val)
            else:
                Values[depth] = [root.val]

            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)

        traverse(root, 0)
        return [value for value in Values.values()]

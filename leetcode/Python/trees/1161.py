# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxSum = root.val 
        maxDepth = 0
        elements = deque([(0,root)])
        sums = {}
        while len(elements) > 0:
            depth, node = elements.popleft()
            if depth in sums:
                sums[depth] += node.val
            else:
                sums[depth] = node.val

            if node.left:
                elements.append((depth+1, node.left))
            if node.right:
                elements.append((depth+1, node.right))
        for depth in sums.keys():
            if maxSum < sums[depth]:
               maxDepth = depth 
               maxSum = sums[depth]
        return maxDepth
        

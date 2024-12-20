# Definition for a binary tree node.
from typing import  List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root, 0)])
        
        nodes = {}
        while len(q) > 0:
            node, depth = q.popleft()
            if depth in nodes:
               nodes[depth].append(node.val) 
            else:
                nodes[depth] = [node.val]

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        result = []
        counter = 0
        for node in nodes.values():
            if counter % 2 != 0:
                node.reverse()
                result.append(node) 
            else:
                result.append(node)
        return result
        

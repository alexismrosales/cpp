# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n^2)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        depth = 0
        # saving a tuple with value and depth
        q = [(root, 0)]
        nodes = {}
        while (len(q) > 0):
            # starting with depth 0 and increasing depth in level
            node, depth = q.pop(0)
            # saving levels in dictionary with their values
            if depth in nodes:
                nodes[depth].append(node.val)
            else:
                nodes[depth] = [node.val]


            # add child nodes in case they exist and increase one level of depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        result = []
        # saving values
        for n in nodes.values():
            result.append(n)
        return result

# O(n)
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        depth = 0
        # in this variation of queue left pop cost O(1) instead of O(n) of a "normal queue" or an array
        q = deque([(root, 0)])
        nodes = {}
        while (len(q) > 0):
            # starting with depth
            node, depth = q.popleft()
            # saving levels in dictionary with their values
            if depth in nodes:
                nodes[depth].append(node.val)
            else:
                nodes[depth] = [node.val]


            # add child nodes in case they exist and increase one level of depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        result = []
        # saving values
        for n in nodes.values():
            result.append(n)
        return result

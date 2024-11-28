# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root):
        self.traverseTree(root)
        return self.balanced

    def traverseTree(self, root):
        if not self.balanced:
            return -1
        if root is None:
            return -1
        lh = self.traverseTree(root.left)
        rh = self.traverseTree(root.right)
        if lh != rh:
            self.balanced = False
        return max(lh, rh) + 1

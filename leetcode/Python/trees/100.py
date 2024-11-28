# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.isEqual = True

    def isSameTree(self, p, q):
        self.traverseTree(p, q)
        return self.isEqual

    def traverseTree(self, p, q):
        # In case the flag has been set just return
        if not self.isEqual:
            return
        if p is None or q is None:
            # If a tree has different size
            if p is None and q or q is None and p:
                self.isEqual = False
            return
        # If any node has different values
        if p.val != q.val:
            self.isEqual = False
            return

        self.traverseTree(p.left, q.left)
        self.traverseTree(p.right, q.right)

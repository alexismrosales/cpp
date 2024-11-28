# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.sideViewnodes = []

    def rightSideView(self, root):
        self.traverseTree(root, 0)
        return self.sideViewnodes

    def traverseTree(self, root, height):
        if root is None:
            return

        # If the level of the height of tree has not been explored, add the node val
        if len(self.sideViewnodes) == height:
            self.sideViewnodes.append(root.val)

        # starting from right
        self.traverseTree(root.right, height + 1)
        self.traverseTree(root.left, height + 1)

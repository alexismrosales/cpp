class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Initialazing a variable to maximize element
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        self.traverseTree(root)
        return self.diameter

    # Traversing in post order
    def traverseTree(self, root):
        if root is None:
            return 0
        leftH = self.traverseTree(root.left)
        rightH = self.traverseTree(root.right)
        self.diameter = max(self.diameter, leftH + rightH)
        return max(leftH, rightH)

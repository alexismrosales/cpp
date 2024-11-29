# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.isSubRoot = False

    def isSubtree(self, root, subRoot):
        self.traverseTree(root, subRoot)
        return self.isSubRoot

    def traverseTree(self, root, subRoot):
        if self.isSubRoot:
            return
        if root is None:
            return
        if self.areEqual(root, subRoot):
            self.isSubRoot = True
        self.traverseTree(root.left, subRoot)
        self.traverseTree(root.right, subRoot)

    def areEqual(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.areEqual(root1.left, root2.left) and self.areEqual(
            root1.right, root2.right
        )


# Better for time
class OtherSolution(object):
    def __init__(self):
        self.tree = ""

    def isSubtree(self, root, subRoot):
        tree = self.stringTree(root)
        subtree = self.stringTree(subRoot)
        return subtree in tree

    def stringTree(self, root):
        if root is None:
            return "$"
        return (
            "#"
            + str(root.val)
            + self.stringTree(root.left)
            + self.stringTree(root.right)
        )

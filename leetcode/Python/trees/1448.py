# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        goodNodesCounter = [0]

        def traverseTree(root, maxNumber):
            if root is None:
                return
            if maxNumber <= root.val:
                goodNodesCounter[0] += 1
            maxNumber = max(maxNumber, root.val)
            traverseTree(root.left, maxNumber)
            traverseTree(root.right, maxNumber)

        traverseTree(root, root.val)
        return goodNodesCounter[0]

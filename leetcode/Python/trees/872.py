from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leavesTree1 = []
        leavesTree2 = []
        def traverseTree(root, tree):
            if root is None:
                return 
            if root.left is None and root.right is None:
                if tree == 1:
                    leavesTree1.append(root.val)
                else:
                    leavesTree2.append(root.val)
                return
            traverseTree(root.left, tree)
            traverseTree(root.right, tree)
        traverseTree(root1, 1)
        traverseTree(root2, 2)
        return leavesTree1 == leavesTree2

class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverseTree(root) -> List[int]:
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [root.val]
            leaves = []
            leaves.extend(traverseTree(root.left))
            leaves.extend(traverseTree(root.right))
            return leaves
        return traverseTree(root1) == traverseTree(root2)


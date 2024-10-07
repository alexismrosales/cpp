package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func traverse(root *TreeNode, level int, maxLevel *int) {
	if root == nil {
		return
	}
	traverse(root.Left, level+1, maxLevel)
	if level > *maxLevel {
		*maxLevel = level
	}
	traverse(root.Right, level+1, maxLevel)
}

func maxDepth(root *TreeNode) int {
	maxLevel := 0
	traverse(root, 1, &maxLevel)
	return maxLevel
}

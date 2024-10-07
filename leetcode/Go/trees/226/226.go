package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertingSides(root *TreeNode) {
	// In case of an empty tree
	if root == nil {
		return
	}
	// Swaping left side with right side
	tmp := root.Left
	root.Left = root.Right
	root.Right = tmp
	// Using preorder traverse
	invertingSides(root.Left)
	invertingSides(root.Right)
}
func invertTree(root *TreeNode) *TreeNode {
	invertedTree := root
	invertingSides(root)
	return invertedTree
}

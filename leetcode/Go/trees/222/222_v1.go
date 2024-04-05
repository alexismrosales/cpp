package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// I would approach this problem usin O(n) complexity
func countNodes(root *TreeNode) int {
	totalNodes := 0
	traverseTree(root, &totalNodes)
	return totalNodes
}

func traverseTree(root *TreeNode, nodes *int) {
	if root == nil {
		return
	}
	*nodes++
	traverseTree(root.Left, nodes)
	traverseTree(root.Right, nodes)
}

package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// The aproach is save the data from left and right trees and compare it
// solution O(2n)

func isSymmetric(root *TreeNode) bool {
	var arrLeft, arrRight []int

	traverseLeft(root.Left, &arrLeft)
	traverseRight(root.Right, &arrRight)

	// If there is a different element
	for i := range len(arrLeft) {
		if arrLeft[i] != arrRight[i] {
			return false
		}
	}
	return true
}

func traverseLeft(root *TreeNode, data *[]int) {
	if root == nil {
		*data = append(*data, -101)
		return
	}
	*data = append(*data, root.Val)
	// Starting from left
	traverseLeft(root.Left, data)
	traverseLeft(root.Right, data)
}

func traverseRight(root *TreeNode, data *[]int) {
	if root == nil {
		*data = append(*data, -101)
		return
	}
	*data = append(*data, root.Val)
	// Starting from right
	traverseRight(root.Right, data)
	traverseRight(root.Left, data)
}

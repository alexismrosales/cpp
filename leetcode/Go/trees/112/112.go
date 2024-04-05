package main

/*
*void Postorder(TreeNode * root, vector<int> &v)
    {
        if(root == nullptr)
            return;
        else
        {
            Postorder(root->left, v);
            Postorder(root->right, v);
            v.push_back(root->val);
        }
    }
*/
// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	hasSum := false
	// If root is null
	if root == nil {
		return false
	}
	traverseTree(root, 0, targetSum, &hasSum)
	return hasSum
}

func traverseTree(root *TreeNode, sum, targetSum int, hasSum *bool) {
	// In case we found a match
	if *hasSum {
		return
	}
	// Setting base recursion
	if root == nil {
		return
	}
	sum += root.Val
	// If we find a leaf node and match the target
	if sum == targetSum && root.Left == nil && root.Right == nil {
		*hasSum = true
	}
	traverseTree(root.Left, sum, targetSum, hasSum)
	traverseTree(root.Right, sum, targetSum, hasSum)
}

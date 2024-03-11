/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
	longestPath := 0
	helper(root, &longestPath)
	return longestPath
}

func helper(node *TreeNode, longestPath *int) int {
	if node == nil {
		return 0
	}

	leftPath := helper(node.Left, longestPath)
	rightPath := helper(node.Right, longestPath)
	*longestPath = max(*longestPath, rightPath+leftPath)
	return max(leftPath, rightPath) + 1
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

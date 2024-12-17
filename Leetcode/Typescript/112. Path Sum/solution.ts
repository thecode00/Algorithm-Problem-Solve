// https://leetcode.com/problems/path-sum/description/

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function hasPathSum(
  root: TreeNode | null,
  targetSum: number,
  curSum: number = 0
): boolean {
  if (!root) {
    return false;
  }

  curSum += root.val;

  if (!root.left && !root.right) {
    return curSum === targetSum;
  }

  return (
    hasPathSum(root.left, targetSum, curSum) ||
    hasPathSum(root.right, targetSum, curSum)
  );
}

// https://leetcode.com/problems/longest-univalue-path/description/

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

function longestUnivaluePath(root: TreeNode | null): number {
  let length = 0;

  function dfs(root: TreeNode | null, parentNum: number): number {
    if (!root) {
      return 0;
    }
    const left = dfs(root.left, root.val),
      right = dfs(root.right, root.val);
    length = Math.max(length, left + right);

    if (root.val !== parentNum) {
      return 0;
    }
    return Math.max(left, right) + 1;
  }

  dfs(root, -1);

  return length;
}

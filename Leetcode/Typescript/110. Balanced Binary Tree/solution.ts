// https://leetcode.com/problems/balanced-binary-tree/description/

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

function isBalanced(root: TreeNode | null): boolean {
  function dfs(root: TreeNode | null): number {
    if (!root) {
      return 0;
    }

    const left = dfs(root.left);
    if (left === -1) {
      return -1;
    }

    const right = dfs(root.right);
    if (right === -1) {
      return -1;
    }

    if (Math.abs(left - right) > 1) {
      return -1;
    }

    return Math.max(left, right) + 1;
  }

  return dfs(root) !== -1;
}

function isBalanced(root: TreeNode | null): boolean {
  let balance = true;

  function dfs(root: TreeNode | null): number {
    if (!root || !balance) {
      return 0;
    }

    const left = dfs(root.left),
      right = dfs(root.right);
    if (Math.abs(left - right) > 1) {
      balance = false;
    }

    return Math.max(left, right) + 1;
  }

  dfs(root);
  return balance;
}

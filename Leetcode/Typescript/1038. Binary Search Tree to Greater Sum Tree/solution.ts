// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

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

function bstToGst(root: TreeNode | null): TreeNode | null {
  let total = 0;

  function dfs(root) {
    if (!root) {
      return;
    }
    dfs(root.right);
    total += root.val;
    root.val = total;
    dfs(root.left);
  }

  dfs(root);
  return root;
}

// Recursion
function bstToGst(root: TreeNode | null): TreeNode | null {
  function dfs(root: TreeNode | null, total: number): number {
    if (!root) {
      return total;
    }

    const right = dfs(root.right, total);
    root.val += right;

    return dfs(root.left, root.val);
  }

  dfs(root, 0);
  return root;
}

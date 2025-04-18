// https://leetcode.com/problems/symmetric-tree/description/

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

function isSymmetric(root: TreeNode | null): boolean {
  if (!root) {
    return true;
  }
  return search(root.left, root.right);
}

function search(root1: TreeNode | null, root2: TreeNode | null): boolean {
  if (!root1 && !root2) {
    return true;
  } else if (!root1 || !root2) {
    return false;
  }

  if (root1.val !== root2.val) {
    return false;
  }

  return search(root1.left, root2.right) && search(root1.right, root2.left);
}

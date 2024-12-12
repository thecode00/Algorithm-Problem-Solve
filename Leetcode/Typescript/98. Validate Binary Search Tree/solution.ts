// https://leetcode.com/problems/validate-binary-search-tree/description/

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

function isValidBST(root: TreeNode | null): boolean {
  let prev = null;
  const bstArray = [];

  // Inorder
  while (root !== null || bstArray.length > 0) {
    while (root !== null) {
      bstArray.push(root);
      root = root.left;
    }

    root = bstArray.pop();
    if (prev !== null && prev >= root.val) {
      return false;
    }

    prev = root.val;
    root = root.right;
  }
  return true;
}

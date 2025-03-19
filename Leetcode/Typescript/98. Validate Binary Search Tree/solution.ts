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

// Recursive
function isValidBST(root: TreeNode | null): boolean {
  return rangeSearch(root, null, null);
}

function rangeSearch(
  root: TreeNode | null,
  minValue: number | null,
  maxValue: number | null
) {
  if (!root) {
    return true;
  }

  if (
    (minValue !== null && root.val <= minValue) ||
    (maxValue !== null && maxValue <= root.val)
  ) {
    return false;
  }

  const left = rangeSearch(root.left, minValue, root.val);
  if (!left) {
    return false;
  }

  const right = rangeSearch(root.right, root.val, maxValue);
  if (!right) {
    return false;
  }

  return true;
}

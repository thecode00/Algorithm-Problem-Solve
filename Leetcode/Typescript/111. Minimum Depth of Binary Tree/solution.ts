// https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

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
const LEAF_DEPTH = Number.MAX_SAFE_INTEGER;

function minDepth(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }

  const leftDepth = root.left ? minDepth(root.left) : LEAF_DEPTH;
  const rightDepth = root.right ? minDepth(root.right) : LEAF_DEPTH;

  // Leaf node
  if (leftDepth === LEAF_DEPTH && rightDepth === LEAF_DEPTH) {
    return 1;
  }

  return Math.min(leftDepth, rightDepth) + 1;
}

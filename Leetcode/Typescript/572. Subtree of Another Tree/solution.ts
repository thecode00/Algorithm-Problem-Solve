// https://leetcode.com/problems/subtree-of-another-tree/description/

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

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  return subTree(root, subRoot);
}

function subTree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  if (!root) {
    return false;
  }
  // If the current node's value matches the subRoot's root value,
  // check if the two subtrees are exactly the same
  if (root.val === subRoot.val && checkSameTree(root, subRoot)) {
    return true;
  }
  // If not found at the current node, continue searching in the left and right subtrees.
  return subTree(root.left, subRoot) || subTree(root.right, subRoot);
}

function checkSameTree(
  root: TreeNode | null,
  subRoot: TreeNode | null
): boolean {
  if (!root && !subRoot) {
    return true;
  }

  if (!root || !subRoot || root.val !== subRoot.val) {
    return false;
  }

  return (
    checkSameTree(root.left, subRoot.left) &&
    checkSameTree(root.right, subRoot.right)
  );
}

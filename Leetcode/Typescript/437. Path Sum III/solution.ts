// https://leetcode.com/problems/path-sum-iii/

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

function pathSum(root: TreeNode | null, targetSum: number): number {
  return search(root, targetSum, new Map<number, number>(), 0);
}

function search(
  root: TreeNode | null,
  targetSum: number,
  pathSumHash: Map<number, number>,
  totalSum: number
): number {
  if (!root) {
    return 0;
  }
  totalSum += root.val;
  const key = totalSum - targetSum;
  let pathCount = pathSumHash.get(key) || 0;

  if (totalSum === targetSum) {
    pathCount += 1;
  }

  savePathCount(pathSumHash, totalSum, 1);
  pathCount += search(root.left, targetSum, pathSumHash, totalSum);
  pathCount += search(root.right, targetSum, pathSumHash, totalSum);
  savePathCount(pathSumHash, totalSum, -1);

  return pathCount;
}

function savePathCount(hash: Map<number, number>, key: number, diff: number) {
  const newPathCount = (hash.get(key) || 0) + diff;

  if (newPathCount === 0) {
    hash.delete(key);
  } else {
    hash.set(key, newPathCount);
  }
}

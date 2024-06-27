// https://leetcode.com/problems/range-sum-of-bst/description/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution { // BruteForce
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {
            return 0;
        }

        int left = rangeSumBST(root.left, low, high);
        int right = rangeSumBST(root.right, low, high);

        int total = left + right;
        if (low <= root.val && root.val <= high) {
            total += root.val;
        }
        return total;
    }
}

class Solution { // BackTracking
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {
            return 0;
        }

        if (root.val < low) {
            return rangeSumBST(root.right, low, high);
        }
        if (root.val > high) {
            return rangeSumBST(root.left, low, high);
        }
        int left = rangeSumBST(root.left, low, high);
        int right = rangeSumBST(root.right, low, high);
        int total = left + right;

        total += root.val;
        return total;
    }
}
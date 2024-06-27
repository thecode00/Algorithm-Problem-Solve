// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

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
class Solution {
    int total = 0;

    public TreeNode bstToGst(TreeNode root) { // In-order
        if (root == null) {
            return null;
        }

        bstToGst(root.right);
        total += root.val;
        root.val = total;
        bstToGst(root.left);

        return root;
    }
}
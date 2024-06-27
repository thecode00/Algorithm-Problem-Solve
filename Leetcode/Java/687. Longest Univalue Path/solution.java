// https://leetcode.com/problems/longest-univalue-path/description/

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
    int longest = 0;

    public int longestUnivaluePath(TreeNode root) {
        this.dfs(-1, root);
        return this.longest;
    }

    private int dfs(int val, TreeNode node) {
        if (node == null) {
            return 0;
        }

        int left = dfs(node.val, node.left);
        int right = dfs(node.val, node.right);
        this.longest = Math.max(this.longest, left + right);

        if (val != node.val) {
            return 0;
        }
        return Math.max(left, right) + 1;
    }
}
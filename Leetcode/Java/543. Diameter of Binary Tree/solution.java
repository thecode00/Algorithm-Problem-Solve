// https://leetcode.com/problems/diameter-of-binary-tree/description/

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

    public int diameterOfBinaryTree(TreeNode root) {
        this.dfs(root);
        return this.longest;
    }

    public int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int left = dfs(node.left);
        int right = dfs(node.right);
        // Check the diameter of the tree with the current node as the root.
        this.longest = Math.max(this.longest, left + right);

        return Math.max(left, right) + 1;
    }
}
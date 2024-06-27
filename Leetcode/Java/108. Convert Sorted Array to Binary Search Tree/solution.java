// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

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
    public TreeNode sortedArrayToBST(int[] nums) {
        return convert(nums, 0, nums.length - 1);
    }

    private TreeNode convert(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }
        // To create a height-balanced tree, the left and right sides should have as
        // similar a number of nodes as possible. Therefore, set the middle of the array
        // as the root and divide the left and right sides.
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = convert(nums, start, mid - 1);
        root.right = convert(nums, mid + 1, end);

        return root;
    }
}
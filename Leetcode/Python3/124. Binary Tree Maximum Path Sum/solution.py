# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def __init__(self) -> None:
        self.max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.get_root_sum(root)
        return self.max_sum

    def get_root_sum(self, root: Optional[TreeNode]) -> int:
        """
        Args:
            root: The root node of the tree for which we want to calculate the path sum

        Returns: 
            Return the largest path sum starting from the current root node.
        """
        if not root:
            return 0

        left, right = max(self.get_root_sum(root.left), 0), max(self.get_root_sum(root.right), 0)
        self.max_sum = max(self.max_sum, left + root.val + right)

        return root.val + max(left, right)

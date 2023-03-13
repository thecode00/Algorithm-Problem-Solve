# https://leetcode.com/problems/symmetric-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetric(left, right):
            if left and right:  # Filter (left and right) for (left or right)
                pass
            elif left or right:
                return False
            else:   # Both None
                return True

            if left.val != right.val:
                return False

            return symmetric(left.left, right.right) and symmetric(left.right, right.left)
        return symmetric(root.left, root.right)

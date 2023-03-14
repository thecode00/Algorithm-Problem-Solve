# https://leetcode.com/problems/sum-root-to-leaf-numbers/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], path: str = "") -> int:
        if root.left == None and root.right == None:    # When root is leaf return int path
            return int(path + str(root.val))
        total = 0
        if root.left:
            total += self.sumNumbers(root.left, path + str(root.val))
        if root.right:
            total += self.sumNumbers(root.right, path + str(root.val))
        return total
        
        
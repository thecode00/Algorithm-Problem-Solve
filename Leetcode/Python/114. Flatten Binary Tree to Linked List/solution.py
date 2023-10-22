# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        prev = None
        stack = [root]
        # Flatten nodes of tree to left.
        while stack:    # DFS
            cur = stack.pop()

            if prev:
                prev.left = cur

            prev = cur

            if cur.right:
                stack.append(cur.right)
                cur.right = None
            if cur.left:
                stack.append(cur.left)

        cur = root
        # Now flatten tree that has been flatten to left, making it flat to right.
        while cur:
            cur.left, cur.right = cur.right, cur.left
            cur = cur.right

        return root

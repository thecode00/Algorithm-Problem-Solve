# https://leetcode.com/problems/minimum-distance-between-bst-nodes/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = float("inf")
    min_diff = float("inf")
    # Min_diff node will root.right node or rightmost node root.left
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.min_diff = min(self.min_diff, abs(root.val - self.prev))
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)
        
        return self.min_diff


            
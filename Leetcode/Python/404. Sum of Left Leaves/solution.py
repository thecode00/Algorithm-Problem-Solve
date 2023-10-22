# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, left):    # Runtime: 37 ms
            if not root:
                return 0
            if left:
                if not root.left and not root.right:    # If root not have child node
                    return root.val
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)
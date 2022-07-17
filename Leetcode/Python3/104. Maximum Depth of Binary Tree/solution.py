# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, depth):
        if root:
            return max(self.dfs(root.left, depth + 1), self.dfs(root.right, depth + 1))
        return depth
    def maxDepth(self, root: Optional[TreeNode]) -> int:    # Runtime: 89 ms
        return self.dfs(root, 0)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:    # Runtime: 56 ms
        def dfs(root, depth):
            if root:
                return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            return depth
        return dfs(root, 0)

    
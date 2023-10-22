# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Recurssive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return 0
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1), depth)
        return dfs(root, 1)

# Use deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):  # Use for loop to pop same depth node
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return depth

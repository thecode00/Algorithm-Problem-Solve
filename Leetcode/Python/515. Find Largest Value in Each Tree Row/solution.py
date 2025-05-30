# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        queue = deque()
        queue.append(root)

        # Search each level and find max value
        while queue:
            size = len(queue)

            max_value = -float("inf")
            for _ in range(size):
                node = queue.popleft()
                max_value = max(max_value, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_value)

        return result

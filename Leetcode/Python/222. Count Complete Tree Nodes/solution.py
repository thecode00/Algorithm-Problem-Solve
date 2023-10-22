# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:  # Time complexity: O(N)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 0
        queue = deque([root])
        while queue:
            length = len(queue)
            count += length
            for _ in range(length):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return count

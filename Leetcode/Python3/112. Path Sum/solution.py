# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:  # BFS
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, 0)])
        while queue:
            cur, total = queue.popleft()
            total += cur.val
            if total == targetSum and not cur.left and not cur.right:
                return True

            if cur.left:
                queue.append((cur.left, total))
            if cur.right:
                queue.append((cur.right, total))

        return False


class Solution:  # Recursive
    # Ref: https://leetcode.com/problems/path-sum/solutions/36360/short-python-recursive-solution-o-n/
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if root.val == targetSum and not root.left and not root.right:
            return True

        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right)

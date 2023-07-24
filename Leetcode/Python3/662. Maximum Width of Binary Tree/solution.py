# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dist = 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            # Compare each level left most ~ right most nodes distance
            dist = max(dist, queue[-1][1] - queue[0][1] + 1)
            length = len(queue)
            for _ in range(length):
                node, num = queue.popleft()
                # In a binary tree, when the node is n, the left child is the node at position n * 2
                # and the right child is the node at position n * 2 + 1.
                if node.left:
                    queue.append((node.left, num * 2))
                if node.right:
                    queue.append((node.right, num * 2 + 1))
        return dist

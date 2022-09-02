# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_total = defaultdict(int)
        node_amount = defaultdict(int)
        answer = []

        def bfs(node, level):
            if node:
                level_total[level] += node.val
                node_amount[level] += 1
                bfs(node.left, level + 1)
                bfs(node.right, level + 1)
        bfs(root, 0)
        for level in level_total:
            answer.append(level_total[level] / node_amount[level])
        return answer

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import defaultdict


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        answer = []

        def bfs(root, level):
            if root:
                l = len(answer)
                if l <= level:   # Append new level list
                    answer.append([root.val])
                else:
                    answer[level].append(root.val)
                for node in root.children:
                    bfs(node, level + 1)
        bfs(root, 0)
        return answer

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        node_dict = defaultdict(list)

        def bfs(root, level):
            if root:
                node_dict[level].append(root.val)
                for node in root.children:
                    bfs(node, level + 1)
        bfs(root, 0)
        # print(node_dict.values())
        return node_dict.values()

# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:  # Recursion
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def post(root: 'Node'):
            if not root:
                return

            for child in root.children:
                post(child)

            result.append(root.val)
        post(root)
        return result

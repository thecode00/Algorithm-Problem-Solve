# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # print(root.children, root.val)
        answer, q = [], root and [root]
        while q:
            node = q.pop()
            answer.append(node.val)
            q += [child for child in node.children[::-1] if child]
        return answer

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/148867/Python-short-iterative-solution-beats-100-66-ms-faster-than-fastest-!


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer, q = [], root and [root]
        while q:
            node = q.pop()
            answer.append(node.val)
            q += [child for child in node.children[::-1] if child]
        return answer

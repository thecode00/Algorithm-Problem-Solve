# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            # Length of each tree level
            length = len(queue)
            for i in range(length):
                cur = queue.popleft()
                # Current node is right end of tree level set next node NULL
                if i == length - 1:
                    cur.next = None
                else:
                    cur.next = queue[0]
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

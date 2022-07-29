# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Ref: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/1654181/C%2B%2BPythonJava-Simple-Solution-w-Images-and-Explanation-or-BFS-%2B-DFS-%2B-O(1)-Optimized-BFS

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        q = deque([root])
        # Fill next node from the right to the left to put null in the rightmost node
        while q:
            nextNode = None
            for _ in range(len(q)):
                now = q.popleft()
                now.next, nextNode = nextNode, now
                if now.right:
                    q.extend([now.right, now.left])
        return root

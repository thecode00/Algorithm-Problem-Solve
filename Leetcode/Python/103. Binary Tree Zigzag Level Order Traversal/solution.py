# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        direct_right = True
        # queue_left = direction left level nodes, queue_right = direction right level nodes
        queue_left, queue_right = [], deque([root])
        tree = []
        while queue_left or queue_right:
            level = []
            if direct_right:
                length = len(queue_right)
                for _ in range(length):
                    cur = queue_right.popleft()
                    level.append(cur.val)
                    if cur.left:
                        queue_left.append(cur.left)
                    if cur.right:
                        queue_left.append(cur.right)

            else:   # Direction left is FILO so use stack
                length = len(queue_left)
                for _ in range(length):
                    cur = queue_left.pop()
                    level.append(cur.val)
                    if cur.right:
                        queue_right.appendleft(cur.right)
                    if cur.left:
                        queue_right.appendleft(cur.left)
            direct_right = not direct_right    # Change direction
            tree.append(level)
        return tree


class Solution:  # Use one deque
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        direct_right = True
        queue = deque([root])
        tree = []
        while queue:
            level = []
            length = len(queue)
            if direct_right:
                for _ in range(length):
                    cur = queue.popleft()
                    level.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)

            else:
                for _ in range(length):
                    cur = queue.pop()
                    level.append(cur.val)
                    if cur.right:
                        queue.appendleft(cur.right)
                    if cur.left:
                        queue.appendleft(cur.left)
            direct_right = not direct_right    # Change direction
            tree.append(level)
        return tree


class Solution:  # Ref: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solutions/749036/python-clean-bfs-solution-explained/
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        result, direction = [], 1

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level[::direction])
            direction *= (-1)
        return result

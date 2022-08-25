# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = [head]
        prev = Node(0)
        while stack:
            cur = stack.pop()
            cur.prev = prev
            prev.next = cur
            prev = cur
            # Stack is LILO and we will connect the child nodes before the next node so we search next node first.
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
        head.prev = None
        return head


        
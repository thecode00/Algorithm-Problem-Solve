# https://leetcode.com/problems/copy-list-with-random-pointer/
# Ref: https://leetcode.com/problems/copy-list-with-random-pointer/solutions/43485/clear-and-short-python-o-2n-and-o-n-solution/?envType=study-plan-v2&envId=top-interview-150

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


from collections import defaultdict


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = defaultdict(lambda: Node(0))
        dic[None] = None
        cur = head
        while cur:
            dic[cur].val = cur.val
            # When a key that is not present in a defaultdict is accessed, a key-default value pair is added to the defaultdict.
            dic[cur].next = dic[cur.next]
            dic[cur].random = dic[cur.random]
            cur = cur.next
        return dic[head]

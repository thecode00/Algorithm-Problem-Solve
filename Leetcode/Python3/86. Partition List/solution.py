# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        partition_root, root = ListNode(0), ListNode(0, head)
        partition_node = partition_root
        prev = root
        cur = head
        while cur:
            if cur.val >= x:
                end = cur
                while end.next and end.next.val >= x:
                    end = end.next
                prev.next = end.next
                # Cut node
                end.next = None
                # Add to partition list
                partition_node.next = cur
                partition_node = end
                # end.next is None or has less than x so search prev.next node
                if prev:
                    cur = prev.next
                else:
                    cur = None
            else:
                prev = prev.next
                cur = cur.next
        prev.next = partition_root.next
        return root.next

# https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        root = cur = ListNode(0)
        for idx in range(len(lists)):
            if lists[idx]:  # Filter blank linked list
                # ListNode cant compare so add index between value and listNode
                heapq.heappush(heap, (lists[idx].val, idx, lists[idx]))
        while heap:
            node = heapq.heappop(heap)  # (value, index, linked list)
            idx = node[1]
            cur.next = node[2]
            cur = cur.next

            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))
        return root.next
